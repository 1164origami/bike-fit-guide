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

# Skill identity and Codex interface sanity checks.
skill_text = skill.read_text(encoding="utf-8") if skill.exists() else ""
meta = re.match(r"\A---\n(.*?)\n---\n", skill_text, flags=re.S)
if not meta:
    errors.append("missing valid SKILL.md frontmatter")
else:
    frontmatter = meta.group(1)
    name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", frontmatter)
    if not name_match or name_match.group(1) != ROOT.name:
        errors.append("Skill name must match directory name")
    if not re.search(r"(?m)^description:\s*(?:>|[^\n]+)$", frontmatter):
        errors.append("Skill description is missing")
    if name_match and len(name_match.group(1)) > 64:
        errors.append("Skill name exceeds length limit")

ui = ROOT / "agents/openai.yaml"
if ui.exists():
    ui_text = ui.read_text(encoding="utf-8")
    if not re.search(r"(?m)^interface:\s*$", ui_text):
        errors.append("Codex UI metadata missing interface section")
    if "$" + ROOT.name not in ui_text:
        errors.append("Codex default prompt must mention $skill-name")

if not (ROOT / "tests/scenarios.md").exists():
    errors.append("Manual skill routing scenarios missing")
dynamic = ROOT / "references/dynamic_fitting.md"
if dynamic.exists():
    d = dynamic.read_text(encoding="utf-8")
    if "屈曲量" not in d or "内角" not in d:
        errors.append("Dynamic joint angles must distinguish internal angle and flexion")

if errors:
    print("Bike-fit skill validation failed:")
    for error in errors:
        print(" - " + error)
    sys.exit(1)

print(f"Bike-fit skill validation passed: {len(MARKDOWN)} Markdown files.")
