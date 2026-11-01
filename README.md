<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Skill-6C5CE7?style=for-the-badge" alt="OpenClaw Skill" />
  <img src="https://img.shields.io/badge/QClaw-Skill-6C5CE7?style=for-the-badge" alt="QClaw Skill" />
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

**Bike Fit Guide** 是一个 OpenClaw / QClaw Skill，基于菲尔·伯特（Phil Burt）《BIKE FIT：骑行姿势设定指南》提供专业的骑行姿势指导。Phil Burt 曾任英国自行车协会（British Cycling）及天空车队（Team Sky）首席理疗师。

**Bike Fit Guide** is an OpenClaw / QClaw Skill providing professional cycling bike fit guidance based on Phil Burt's *BIKE FIT* methodology. Phil Burt served as head physiotherapist for British Cycling and Team Sky.

> ⚠️ **OpenClaw / QClaw Skill** — 为 AI 助手在 OpenClaw / QClaw 生态中提供结构化骑行姿势与舒适度知识。触发关键词：bike fit、骑行姿势、车座、锁片、骑行疼痛等。
>
> ⚠️ **OpenClaw / QClaw Skill** — provides structured cycling posture and comfort knowledge for AI assistants in the OpenClaw / QClaw ecosystem. Triggered by keywords: bike fit, cycling posture, saddle, cleats, cycling pain, etc.

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

## 📦 安装 · Installation

### 依赖 · Requirements

本 Skill 为纯知识型（Markdown），无需额外依赖。

This is a knowledge-only Skill (Markdown), no additional dependencies required.

### For OpenClaw / QClaw

```bash
# Option A: Git Clone（推荐 · Recommended）
git clone https://github.com/1164origami/bike-fit-guide.git ~/.qclaw/skills/bike-fit-guide

# Option B: 手动复制 · Manual Copy
cp -r bike-fit-guide/ ~/.qclaw/skills/

# Option C: OpenClaw workspace
cp -r bike-fit-guide/ <your-openclaw-workspace>/skills/
```

当对话涉及骑行姿势、bike fit、舒适度等关键词时，AI 助手会自动加载此技能。

The AI assistant auto-loads this skill when triggered by cycling posture, bike fit, or comfort-related keywords.

---

## 🗂️ 文件结构 · Structure

```
bike-fit-guide/
├── SKILL.md                              # 核心技能定义 · Core skill definition
├── README.md                             # 本文件 · This file
├── LICENSE                               # MIT License
├── .gitignore
└── references/                           # 参考知识库 · Reference knowledge base
    ├── bike-fit-parameters.md            # 参数与角度标准 · Parameters & angle standards
    ├── common-misconceptions.md          # 常见骑行误区 · Common misconceptions
    ├── dynamic_fitting.md                # 动态 Bike Fit · Dynamic fitting
    ├── flexibility-and-recording.md      # 柔韧性训练 · Flexibility training
    ├── injury_prevention.md
    └── symptom_led_fit.md                # 骑姿+症状+训练数据的联合复测流程              # 伤病预防与康复 · Injury prevention & rehab
```

---

## 🚀 使用示例 · Usage

当用户提出以下问题时，AI 会自动加载此技能：

When the user asks any of the following, the AI loads this skill:

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
  <sub>Built for OpenClaw & QClaw</sub>
</p>

## 2026-11 更新：症状驱动与跨平台联动

新增 [症状驱动 Bike Fit 复测流程](references/symptom_led_fit.md)，可结合经用户授权的高驰/COROS、Intervals.icu运动记录与主观疼痛、RPE、坐垫变更历史，制定**复测优先级、单变量调整方案和短骑验证步骤**。本Skill本身不会自动连接账户，也不能替代医生诊断。

本次安全修订重点：明确膝关节角度的两种记法、移除将10–15°坐垫下倾作为常规腰痛处方的误用、移除固定剂量自行服用NSAIDs的建议、改正「视频分析解决80%问题」「75%伤病来自装备」之类证据不足的百分比，避免强制压痛性泡沫轴。公开仓库不得上传私人运动记录、全GPS路线或身份信息。
