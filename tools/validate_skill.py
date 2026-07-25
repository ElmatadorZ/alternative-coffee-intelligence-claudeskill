#!/usr/bin/env python3
"""
validate_skill.py — integrity checks for Alternative Coffee Intelligence.

READ-ONLY. Never modifies SKILL.md. This is a single-file skill, so the checks
hold the markdown to the contract it advertises.

Run:  python tools/validate_skill.py
Exit: 0 pass · 1 fail
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # pragma: no cover
    pass

try:
    import yaml
except ImportError:
    print("Missing dependency: pyyaml. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REQUIRED = ["name", "description"]

results: list[tuple[str, bool]] = []


def check(name: str, cond) -> None:
    results.append((name, bool(cond)))
    print(f"  {'PASS' if cond else 'FAIL'}  {name}")


def main() -> int:
    if not SKILL.exists():
        print(f"FATAL: SKILL.md not found at {SKILL}")
        return 1
    text = SKILL.read_text(encoding="utf-8")

    print("\nINSTALLABILITY")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    check("frontmatter present and delimited", m is not None)
    if not m:
        return 1
    try:
        fm = yaml.safe_load(m.group(1))
        check("frontmatter is valid YAML", isinstance(fm, dict))
    except yaml.YAMLError:
        check("frontmatter is valid YAML", False)
        return 1

    for f in REQUIRED:
        check(f"frontmatter has '{f}'", f in fm)
    check("name is slug-safe (a-z0-9-)",
          bool(re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm.get("name", "")))))
    check("frontmatter declares 'license'", "license" in fm)
    # This project is deliberately public-domain — farming knowledge should be free.
    check("license is CC0-1.0 (matches LICENSE file)",
          str(fm.get("license", "")).upper().replace(" ", "-") == "CC0-1.0")
    check("canonical filename is SKILL.md", SKILL.name == "SKILL.md")

    meta = fm.get("metadata", {}) if isinstance(fm.get("metadata"), dict) else {}
    check("metadata.compatibility declared", bool(meta.get("compatibility")))
    check("metadata.not_for bounds the scope", bool(meta.get("not_for")))

    body = text[m.end():]
    print("\nINTEGRITY")
    check("execution protocol declared", re.search(r"execution protocol", body, re.I) is not None)
    check("first-principle grounding stated",
          re.search(r"first principle", body, re.I) is not None)
    check("scientific-honesty section present",
          re.search(r"scientific honesty", body, re.I) is not None)
    check("diagnosis framed as hypothesis, not verdict",
          re.search(r"hypothesis, not a verdict|not a verdict", body, re.I) is not None)
    check("abstain / [UNVERIFIED] discipline present",
          re.search(r"\[UNVERIFIED\]|name the Unknown", body, re.I) is not None)

    print("\nREPOSITORY")
    check("LICENSE exists", (ROOT / "LICENSE").exists())
    lic = (ROOT / "LICENSE").read_text(encoding="utf-8") if (ROOT / "LICENSE").exists() else ""
    check("LICENSE is CC0", "CC0" in lic)

    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    print(f"\n{'=' * 52}\nVALIDATION: {passed}/{total} passed")
    if passed != total:
        print("FAILED:", [n for n, ok in results if not ok])
        return 1
    print(f"{SKILL.name} is installable and structurally intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
