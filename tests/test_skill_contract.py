"""The Alternative Coffee Intelligence contract.

A single-file skill. The tests hold SKILL.md to the guarantees it makes — the
mode-based execution protocol, the first-principle grounding, and above all the
scientific honesty that keeps a text-based diagnosis from being treated as a lab
result.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def _split():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "frontmatter must be present and delimited"
    return yaml.safe_load(m.group(1)), text[m.end():]


def test_canonical_filename():
    assert SKILL.exists() and SKILL.name == "SKILL.md"


def test_frontmatter_and_cc0_license():
    fm, _ = _split()
    for f in ("name", "description", "license"):
        assert f in fm
    # Public domain on purpose — farming knowledge should belong to the farmers.
    assert str(fm["license"]).upper().replace(" ", "-") == "CC0-1.0"


def test_license_file_is_cc0():
    assert "CC0" in (ROOT / "LICENSE").read_text(encoding="utf-8")


def test_name_slug_safe():
    fm, _ = _split()
    assert re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm["name"]))


def test_metadata_bounds_scope():
    fm, _ = _split()
    meta = fm.get("metadata", {})
    assert meta.get("compatibility")
    assert meta.get("not_for")


def test_execution_protocol_and_first_principle():
    _, body = _split()
    assert re.search(r"execution protocol", body, re.I)
    assert re.search(r"first principle", body, re.I)


def test_diagnosis_is_a_hypothesis_not_a_verdict():
    _, body = _split()
    assert re.search(r"not a verdict", body, re.I)


def test_abstain_over_fabricate():
    _, body = _split()
    assert re.search(r"\[UNVERIFIED\]|name the Unknown", body, re.I)
