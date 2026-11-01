#!/usr/bin/env python3
"""Check Markdown-only Bike Fit Skill integrity and safety regression patterns."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = list(ROOT.rglob("*.md"))
errors = []
skill = ROOT / "SKILL.md"
if not skill.exists() or not skill.read_text(encoding="utf-8").startswith("---\n"):
    errors.append("missing or malformed SKILL.md frontmatter")

pat = re.compile(r"\]\(([^)]+)\)")
for doc in MARKDOWN:
    content = doc.read_text(encoding="utf-8")
    for href in pat.findall(content):
        if href.startswith(("https://", "http://", "mailto:", "#")):
            continue
        relative = href.split("#", 1)[0].split("?", 1)[0]
        if relative and not (doc.parent / relative).resolve().exists():
            errors.append(f"{doc.relative_to(ROOT)} -> missing {relative}")

content = "\n".join(p.read_text(encoding="utf-8") for p in MARKDOWN)
banned = {
    "inverted knee extension angle": r"<140°太高，>150°太低",
    "non-individualized NSAID dosing": r"布洛芬400mg",
    "dangerous no-hands cycling test": r"双手脱把骑行上坡",
    "extreme saddle tilt as universal fix": r"鼻端下降\s*10-15°\s*\|\s*可使腰痛减少",
}
for label, pattern in banned.items():
    if re.search(pattern, content):
        errors.append(label)
if not (ROOT / "references/symptom_led_fit.md").exists():
    errors.append("missing symptom-driven fitting protocol")

# Codex-first discoverability and legacy-brand regression checks
if not (ROOT / "agents/openai.yaml").exists():
    errors.append("missing optional Codex interface metadata expected by this repository")
if re.search(r"(?i)(?:openclaw|qclaw|\\.qclaw)", content):
    errors.append("outdated platform branding in Markdown")
if not (ROOT / "AGENTS.md").exists():
    errors.append("missing Codex maintenance guidance")

if errors:
    print("Bike-fit skill validation failed:")
    for error in errors:
        print(" - " + error)
    sys.exit(1)

print(f"Bike-fit skill validation passed: {len(MARKDOWN)} Markdown files.")
