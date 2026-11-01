# Codex repository maintenance guide

本仓库是 **Codex-first、兼容开放 Agent Skills 标准**的独立技能。修改此仓库时：

- 保留根目录唯一的 `SKILL.md` 和 frontmatter 的 `name` / `description`；不要让说明过长导致技能发现失效。
- `SKILL.md` 保留轻量流程与安全边界；理论、测角数据、具体示例放在 `references/`。
- 请维护 `README.md` 中的 Codex 安装、调用方法与文件结构；不要重新引入废弃工具的安装命令和品牌定位。
- 对腰椎正中痛、持续神经麻木、握力下降或其他危险症状保留先停止诱发运动、必要时就医的规则。Bike Fit 不等于诊断；未知条件下不得给极端坐垫倾角或固定药物处方。
- 涉及 COROS / Intervals.icu 的整合必须经用户授权，保持默认只读。不要把真实个人数据、GPS轨迹或账户凭据写入公开仓库。
- 完成改动后运行 `python tests/validate_skill.py`；同时检查 Markdown 相对链接，以及 `agents/openai.yaml` 的可读性。
- 遇到与功率训练的交叉议题，请参考另一个仓库 `1164origami/cycling-power-coach`，但不要重复复制其中的整个参考内容。
