"""First-line candidate detection, never a privacy guarantee.

Only the JSON Schema keywords implemented here are accepted. Unknown keywords
fail closed. Scan diagnostics contain locations and rule codes, never values.
Synthetic test candidates must be assembled at runtime, not stored as fixtures.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
import ipaddress
import json
import os
from pathlib import Path
import re
from urllib.parse import urlsplit


@dataclass(frozen=True)
class Finding:
    path: str
    code: str
    line: int = 0


KEYWORDS = {"$schema", "title", "description", "type", "additionalProperties", "required", "properties", "pattern", "minLength", "maxLength", "enum", "const", "format", "items", "maxItems", "uniqueItems", "if", "then"}
PATTERNS = {
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "PHONE": r"(?<![\w])(?:\+[1-9]\d{0,2}[ -]?)?(?:\(\d{2,4}\)|\d{2,4})[ -]\d{2,4}[ -]\d{3,4}(?![\w])",
    "INTERNATIONAL_PHONE": r"(?<!\w)\+[1-9]\d{8,14}(?!\w)",
    "DOMESTIC_PHONE": r"(?<!\w)0(?:[789]0\d{8}|[1-9]\d{8})(?!\w)",
    "PRIVATE_KEY": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----",
    "API_KEY": r"\b(?:sk-[A-Za-z0-9_-]{20,}|AIza[A-Za-z0-9_-]{30,}|AKIA[A-Z0-9]{16})\b",
    "ACCESS_TOKEN": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{15,})\b",
    "JWT": r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b",
    "DANGEROUS_ASSIGNMENT": r"(?i)\b(?:password|passwd|secret|token|api[_-]?key|access[_-]?token)\b[\"']?\s*[:=]\s*[\"'][^\"'\r\n]{4,}[\"']",
    "UNQUOTED_CREDENTIAL": r"(?im)^\s*(?:password|passwd|secret|token|api[_-]?key|access[_-]?token)\s*[:=]\s*[A-Za-z0-9_+/.-]{4,}\s*$",
    "BEARER_TOKEN": r"(?i)\bBearer\s+[A-Za-z0-9_.+/=-]{16,}",
    "PERSONAL_URL": r"(?i)https?://(?:www\.)?(?:x\.com|twitter\.com|facebook\.com|instagram\.com|linkedin\.com|tiktok\.com|discord\.com|discord\.gg)/[^\s<>\"']+",
    "PROFILE_URL": r"(?i)https?://(?:github\.com/[A-Za-z0-9_-]+/?(?=[\s<>\"']|$)|gist\.github\.com/[^\s<>\"']+)",
}
FORBIDDEN_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".mp3", ".wav", ".mp4", ".pdf", ".zip", ".7z", ".pem", ".key", ".p12", ".pfx", ".log", ".sqlite", ".db"}
FORBIDDEN_NAMES = {".env", "credentials", "id_rsa", "id_ed25519", "cookies.txt", "chat_export.json", "transcript.txt", "terminal.log"}


def schema_errors(value, schema: dict, location: str = "$") -> list[str]:
    """Return value-free error locations for the explicitly supported subset."""
    errors = []
    if unsupported_schema(schema):
        return [location + ":unsupported-schema"]
    kind = schema.get("type")
    predicates = {"object": lambda v: isinstance(v, dict), "array": lambda v: isinstance(v, list), "string": lambda v: isinstance(v, str), "boolean": lambda v: isinstance(v, bool), "integer": lambda v: isinstance(v, int) and not isinstance(v, bool), "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool), "null": lambda v: v is None}
    if kind is not None and (kind not in predicates or not predicates[kind](value)):
        return [location + ":type"]
    if "const" in schema and (type(value) != type(schema["const"]) or value != schema["const"]):
        errors.append(location + ":const")
    if "enum" in schema and not any(type(value) == type(v) and value == v for v in schema["enum"]):
        errors.append(location + ":enum")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append(location + ":required")
        if schema.get("additionalProperties") is False and set(value) - set(props):
            errors.append(location + ":additional-properties")
        for key, child in props.items():
            if key in value:
                errors.extend(schema_errors(value[key], child, location + "." + key))
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0) or len(value) > schema.get("maxLength", float("inf")):
            errors.append(location + ":length")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            errors.append(location + ":pattern")
        fmt = schema.get("format")
        if fmt == "date":
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    raise ValueError()
                date.fromisoformat(value)
            except ValueError:
                errors.append(location + ":date")
        elif fmt == "safe-source-uri":
            try:
                parsed = urlsplit(value)
                parsed.port  # Validate port syntax/range even when no port is needed.
                if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
                    raise ValueError()
                try:
                    ipaddress.ip_address(parsed.hostname)
                except ValueError:
                    pass
                else:
                    raise ValueError()
            except ValueError:
                errors.append(location + ":source-uri")
        elif fmt is not None:
            errors.append(location + ":unsupported-format")
    if isinstance(value, list):
        if len(value) > schema.get("maxItems", float("inf")):
            errors.append(location + ":max-items")
        if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            errors.append(location + ":unique-items")
        for index, item in enumerate(value):
            if "items" in schema:
                errors.extend(schema_errors(item, schema["items"], location + "[" + str(index) + "]"))
    if "if" in schema and not schema_errors(value, schema["if"], location):
        errors.extend(schema_errors(value, schema.get("then", {}), location))
    return errors


def unsupported_schema(schema, depth=0):
    """Reject unsupported keywords and malformed keyword values without crashing."""
    if depth > 64 or not isinstance(schema, dict) or set(schema) - KEYWORDS:
        return True
    for key in ("$schema", "title", "description", "pattern", "format", "type"):
        if key in schema and not isinstance(schema[key], str):
            return True
    if "type" in schema and schema["type"] not in {"object", "array", "string", "boolean", "integer", "number", "null"}:
        return True
    if "format" in schema and schema["format"] not in {"date", "safe-source-uri"}:
        return True
    if "$schema" in schema and schema["$schema"] != "https://json-schema.org/draft/2020-12/schema":
        return True
    for key in ("additionalProperties", "uniqueItems"):
        if key in schema and not isinstance(schema[key], bool):
            return True
    for key in ("minLength", "maxLength", "maxItems"):
        if key in schema and (type(schema[key]) is not int or schema[key] < 0):
            return True
    if schema.get("minLength", 0) > schema.get("maxLength", float("inf")):
        return True
    if "pattern" in schema:
        try:
            re.compile(schema["pattern"])
        except re.error:
            return True
    if "required" in schema:
        required = schema["required"]
        if not isinstance(required, list) or any(not isinstance(v, str) for v in required) or len(set(required)) != len(required):
            return True
    if "enum" in schema:
        options = schema["enum"]
        if not isinstance(options, list) or not options:
            return True
        try:
            if len({json.dumps(v, sort_keys=True, allow_nan=False) for v in options}) != len(options):
                return True
        except (TypeError, ValueError):
            return True
    if "properties" in schema and (not isinstance(schema["properties"], dict) or any(not isinstance(k, str) for k in schema["properties"])):
        return True
    return any(unsupported_schema(v, depth + 1) for v in schema.get("properties", {}).values()) or any(unsupported_schema(schema[k], depth + 1) for k in ("items", "if", "then") if k in schema)


def scan_text(text: str, path: str = "<memory>") -> list[Finding]:
    results = []
    for code, pattern in PATTERNS.items():
        for match in re.finditer(pattern, text):
            results.append(Finding(path, code, text.count("\n", 0, match.start()) + 1))
    # Address syntax is checked with ipaddress to reduce numeric false positives.
    for match in re.finditer(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|(?<![\w:])[0-9A-Fa-f:]*:[0-9A-Fa-f:]+(?:%[\w]+)?(?![\w:])", text):
        try:
            ipaddress.ip_address(match.group())
        except ValueError:
            continue
        results.append(Finding(path, "IP_ADDRESS", text.count("\n", 0, match.start()) + 1))
    if len(text.encode("utf-8")) > 65536 and len(re.findall(r"(?im)^\s*(?:user|assistant|system|human|agent)\s*:", text)) >= 10:
        results.append(Finding(path, "RAW_TRANSCRIPT"))
    return results


def _load_json(text):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate-key")
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=unique_pairs, parse_constant=lambda _: (_ for _ in ()).throw(ValueError("nonfinite")))


def scan_json(value, path: str) -> list[Finding]:
    """Scan decoded keys/strings and associations so escaping cannot hide candidates."""
    codes = set()
    conversation_roles = 0

    def visit(node):
        nonlocal conversation_roles
        if isinstance(node, str):
            codes.update(f.code for f in scan_text(node, path))
        elif isinstance(node, dict):
            if node.get("role") in ("user", "assistant", "system", "human", "agent"):
                conversation_roles += 1
            for key, child in node.items():
                visit(key)
                visit(child)
        elif isinstance(node, list):
            for child in node:
                visit(child)

    visit(value)
    # Decoded key/value associations also reveal credential assignments.
    decoded_text = json.dumps(value, ensure_ascii=False, allow_nan=False)
    codes.update(f.code for f in scan_text(decoded_text, path))
    if len(decoded_text.encode("utf-8")) > 65536 and conversation_roles >= 10:
        codes.add("RAW_TRANSCRIPT")
    return [Finding(path, code, 0) for code in sorted(codes)]


def validate_repository(root: Path | str) -> tuple[list[Finding], int]:
    root = Path(root)
    findings = []
    entries = []
    try:
        schema_path = root / "schema/experience-entry.schema.json"
        for candidate in (root, root / "schema", schema_path):
            if candidate.is_symlink() or (hasattr(candidate, "is_junction") and candidate.is_junction()):
                return [Finding("schema/experience-entry.schema.json", "SYMLINK")], 0
        schema = _load_json(schema_path.read_text(encoding="utf-8"))
        if unsupported_schema(schema):
            raise ValueError("unsupported-schema")
    except (OSError, UnicodeError, ValueError, TypeError, AttributeError, RecursionError):
        return [Finding("schema/experience-entry.schema.json", "SCHEMA_DEFINITION")], 0
    paths = []
    def walk_error(error):
        findings.append(Finding("<unreadable-directory>", "UNREADABLE_DIRECTORY"))
    for directory, subdirs, filenames in os.walk(root, topdown=True, followlinks=False, onerror=walk_error):
        directory_path = Path(directory)
        for dirname in list(subdirs):
            child = directory_path / dirname
            if directory_path == root and dirname == ".git":
                subdirs.remove(dirname)
                continue
            if child.is_symlink() or (hasattr(child, "is_junction") and child.is_junction()):
                paths.append(child)
                subdirs.remove(dirname)
        paths.extend(directory_path / name for name in filenames)
    for item in sorted(paths):
        relative = item.relative_to(root)
        if relative.parts[0] == ".git":
            continue
        path = relative.as_posix()
        if item.is_symlink() or (hasattr(item, "is_junction") and item.is_junction()):
            findings.append(Finding(path, "SYMLINK"))
            continue
        if not item.is_file():
            continue
        if item.suffix.lower() in FORBIDDEN_EXTENSIONS or item.name.lower() in FORBIDDEN_NAMES or item.name.lower().startswith(".env."):
            findings.append(Finding(path, "FORBIDDEN_FILE"))
        try:
            if item.stat().st_size > 1048576:
                findings.append(Finding(path, "OVERSIZED_FILE"))
                continue
            text = item.read_text(encoding="utf-8")
            if "\x00" in text:
                raise UnicodeError()
        except (OSError, UnicodeError):
            findings.append(Finding(path, "UNREADABLE_OR_BINARY"))
            continue
        findings.extend(scan_text(text, path))
        parsed_json = None
        if item.suffix.lower() == ".json":
            try:
                parsed_json = _load_json(text)
                findings.extend(scan_json(parsed_json, path))
            except (ValueError, TypeError, UnicodeError, RecursionError):
                findings.append(Finding(path, "INVALID_JSON"))
                continue
        if relative.parts[0] != "knowledge" or item.name == ".gitkeep":
            continue
        if item.suffix.lower() != ".json":
            findings.append(Finding(path, "KNOWLEDGE_FORMAT"))
            continue
        try:
            entry = parsed_json
            errors = schema_errors(entry, schema)
            if errors:
                findings.append(Finding(path, "SCHEMA_VIOLATION"))
                continue
            if len(relative.parts) != 3 or relative.parts[1] != entry["category"]:
                findings.append(Finding(path, "CATEGORY_PATH"))
            entries.append((path, entry))
        except (ValueError, TypeError, KeyError):
            findings.append(Finding(path, "INVALID_JSON"))
    ids = [entry["id"] for _, entry in entries]
    for path, entry in entries:
        if ids.count(entry["id"]) > 1:
            findings.append(Finding(path, "DUPLICATE_ID"))
        if any(ref not in ids or ref == entry["id"] for ref in entry["related_knowledge_ids"]):
            findings.append(Finding(path, "RELATED_ID"))
    return findings, len(entries)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    findings, count = validate_repository(args.root)
    for finding in findings:
        # File names may contain unsafe text; show only a numbered location.
        safe_path = finding.path if not scan_text(finding.path) and not any(ord(c) < 32 for c in finding.path) else "<unsafe-filename>"
        print(f"{safe_path}:{finding.line}: {finding.code}")
    print(f"{'FAIL' if findings else 'PASS'}: {count} knowledge entries; automated validation != privacy guarantee")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
