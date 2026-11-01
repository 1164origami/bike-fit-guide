<p align="center">
  <img src="https://img.shields.io/badge/Codex-Skill-0A73B8?style=for-the-badge" alt="Codex Skill" />
  <img src="https://img.shields.io/badge/Agent_Skills-Open_Standard-2A9D8F?style=for-the-badge" alt="Agent Skills" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
</p>

<h1 align="center">🚴 Bike Fit Guide</h1>
<h3 align="center">骑行姿势设定指南</h3>
<h3 align="center"><i>Cycling Posture & Fit Optimization</i></h3>

<p align="center">
  Based on Phil Burt's <i>BIKE FIT</i> methodology
  <br/>
  基于菲尔·伯特《BIKE FIT：骑行姿势设定指南》
</p>

---

## 📖 简介 · Introduction

**Bike Fit Guide** 是一个以 **OpenAI Codex** 为主要使用环境、兼容开放 Agent Skills 规范的骑行姿势优化知识型 Skill。参考 Phil Burt 的 Bike Fit 框架，帮助骑行者排查坐垫、车把、锁片、腰背/手部压力等问题，并设计可验证的微调流程。

**Bike Fit Guide** is a Codex-first, portable Agent Skill for individualized bicycle fit and riding comfort. It combines symptom-led assessment, bike setup references and gradual, one-variable-at-a-time validation.

> **边界**：本 Skill 是骑姿与训练辅助资料，不能替代运动医学诊断；出现持续腰椎正中疼痛、神经麻木或危险症状，应优先进行相应评估。与训练负荷分析有关的问题可结合 [cycling-power-coach](https://github.com/1164origami/cycling-power-coach) 使用。

---

## ✨ 功能 · Features

| Feature · 功能 | Description · 说明 |
|---------------|-------------------|
| 🔍 疼痛诊断<br>Pain Diagnosis | 按疼痛部位系统排查（脚/膝/髋/腰/颈/手/会阴）<br>Systematic diagnosis by pain location (foot/knee/hip/back/neck/hand/perineum) |
| 📐 姿势调整<br>Posture Adjustment | 车座高度/前后、车把、锁片设定指南<br>Saddle height/fore-aft, handlebar, cleat setup guide |
| 🚑 伤病预防<br>Injury Prevention | 膝盖疼痛、ITBS、会阴麻木、下背痛、手麻<br>Knee pain, ITBS, numbness, lower back pain, hand numbness |
| 🧘 柔韧性训练<br>Flexibility | 针对性拉伸和泡沫轴方案<br>Targeted stretching & foam roller protocols |
| 📏 参数速查<br>Quick Reference | 关节角度标准（Retül 动态测量）<br>Joint angle standards (Retül dynamic measurement) |
| ❌ 误区纠正<br>Myth Busting | 常见骑行姿势误区科学解析<br>Science-based correction of common cycling myths |
| 🏎️ 车型专项<br>Bike-Specific | 公路车 / TT / 铁三 / 山地 / 场地<br>Road / TT / Triathlon / MTB / Track |

---

## 📦 在 Codex 中安装 · Installation

本仓库采用标准 `SKILL.md` + `references/` 结构。个人级安装目录使用 **`$HOME/.agents/skills/`**，不依赖额外包或常驻进程。可直接安装至 Codex CLI、IDE 扩展使用的本地 Skill 目录。

### Windows PowerShell（推荐）

```powershell
$skillsRoot = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
git clone https://github.com/1164origami/bike-fit-guide.git (Join-Path $skillsRoot "bike-fit-guide")
```

如果已经克隆过，使用 `git -C (Join-Path $HOME '.agents\skills\bike-fit-guide') pull --ff-only` 更新，不要重复克隆。

### macOS / Linux

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/1164origami/bike-fit-guide.git "$HOME/.agents/skills/bike-fit-guide"
```

若仅希望某个代码项目使用，可克隆到该项目的 `.agents/skills/bike-fit-guide/`。

### 在 Codex 中调用

- 显式调用：输入 `$bike-fit-guide`，或者用 `/skills` 选择该 Skill。
- 隐式调用：Codex **可能**根据 `SKILL.md` 的 `description` 自动选择；不要把关键词匹配理解为每次都会强制触发。
- 示例：`使用 $bike-fit-guide 对比新旧坐垫后的骑姿变化，重点检查腰背压力、手腕承重和动态复测方案。`
- 本地更新若没有立即显示，可重启 Codex；参考 [Codex Skills 官方文档](https://developers.openai.com/codex/skills)。

### 运动数据的使用边界

可以与**另行获得授权**的 COROS/高驰、Intervals.icu 数据配合；本 Skill 本身不会自动连接账户、收集个人运动数据或修改设备设置。公开仓库禁止写入个人运动日志、完整GPS轨迹或访问令牌。

---
## 🗂️ 文件结构 · Structure

```text
bike-fit-guide/
├── SKILL.md                    # Codex Skill 描述和工作流程
├── README.md                   # 安装和项目说明
├── AGENTS.md                   # Codex 维护仓库时的约束
├── agents/openai.yaml          # 可选的 Codex 展示元数据
├── references/
│   ├── bike-fit-parameters.md
│   ├── common-misconceptions.md
│   ├── dynamic_fitting.md
│   ├── flexibility-and-recording.md
│   ├── injury_prevention.md
│   └── symptom_led_fit.md
├── tests/validate_skill.py     # 链接/规则静态校验
└── .github/workflows/skill-validation.yml
```

---
## 🚀 使用示例 · Usage

以下是适合用 `$bike-fit-guide` 显式触发的典型场景；自然语言提问也可能被 Codex 自动匹配：

| 中文 | English |
|------|---------|
| "我骑车膝盖疼怎么办" | "My knee hurts when cycling" |
| "怎么调整车座高度" | "How to set saddle height" |
| "锁片应该怎么装" | "How to position cleats" |
| "骑久了手麻怎么回事" | "Why do my hands go numb after long rides" |
| "公路车应该用什么姿势" | "What posture for road cycling" |
| "ITBS 怎么恢复" | "How to recover from ITBS" |
| "怎么提高气动姿势" | "How to improve aero position" |

---

## 📚 知识来源 · Knowledge Source

| Source · 来源 | Content · 内容 |
|--------------|---------------|
| **Phil Burt** | *BIKE FIT* (2nd Ed.) — 自行车及天空车队首席理疗师<br>*BIKE FIT* (2nd Ed.) — head physio for British Cycling & Team Sky |
| **Retül** | 3D 动态测量系统角度标准<br>3D dynamic fitting system joint angle standards |
| **UCI** | 国际自行车联盟器材与姿势规则<br>Union Cycliste Internationale equipment & position regulations |

---

## 📄 许可协议 · License

MIT © [1164origami](https://github.com/1164origami)

---

<p align="center">
  <sub>为骑行者打造，由骑行者打造 · Made for cyclists, by cyclists</sub>
  <br/>
  <sub>Codex-first · Open Agent Skills</sub>
</p>

## 🧩 近期方法论更新：症状驱动与跨平台联动

新增 [症状驱动 Bike Fit 复测流程](references/symptom_led_fit.md)，可结合经用户授权的高驰/COROS、Intervals.icu运动记录与主观疼痛、RPE、坐垫变更历史，制定**复测优先级、单变量调整方案和短骑验证步骤**。本Skill本身不会自动连接账户，也不能替代医生诊断。

本次安全修订重点：明确膝关节角度的两种记法、移除将10–15°坐垫下倾作为常规腰痛处方的误用、移除固定剂量自行服用NSAIDs的建议、改正「视频分析解决80%问题」「75%伤病来自装备」之类证据不足的百分比，避免强制压痛性泡沫轴。公开仓库不得上传私人运动记录、全GPS路线或身份信息。
