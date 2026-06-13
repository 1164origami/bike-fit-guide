<p align="center">
  <img src="https://img.shields.io/badge/OpenClaw-Skill-6C5CE7?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNy45M2MtMy45NS0uNDktNy0zLjg1LTctNy45MyAwLS40NC4wNC0uODguMTEtMS4zMS4yNy45NC42MyAxLjgyIDEuMDcgMi42MS4yNi40Ny41NC45NC44NCAxLjM4LjMtLjguNjMtMS42IDEuMDItMi4zOC4xOC0uMzYuMzctLjcyLjU4LTEuMDguMzctLjc2Ljc4LTEuNTEgMS4yNC0yLjI1LjI3LS40Ni41Ni0uOTEuODYtMS4zNS4xNS0uMjEuMzEtLjQyLjQ3LS42My4wMS0uMDEuMDItLjAyLjAzLS4wMy0uMDEgMC0uMDIgMC0uMDMgMGguMDFjMS41NiAwIDMuMDMuNTYgNC4xNyAxLjU4LS43Mi0uMTQtMS40Ny0uMjItMi4yMy0uMjItLjQgMC0uNzkuMDMtMS4xOC4wOS4yNS0uMjcuNTEtLjUzLjc5LS43OC4xLS4wOS4yMS0uMTcuMzEtLjI1LS4wMSAwLS4wMiAwLS4wMyAwLS4wMSAwLS4wMiAwLS4wMyAwem0tMy4wMSA0Ljg2Yy0uODctLjctMS41OC0xLjYxLTIuMDYtMi42Ni0uMjctLjU5LS40OC0xLjIxLS42My0xLjg2LS4wMS0uMDMtLjAyLS4wNy0uMDMtLjEgMS4yNiAxLjY3IDIuOTkgMi44NyA0Ljk5IDMuMzktLjczLjM4LTEuNTMuNjEtMi4zNy42MS0uNTggMC0xLjE0LS4xMS0xLjY1LS4zMS0uMDgtLjAzLS4xNy0uMDctLjI1LS4xMXoiLz48L3N2Zz4=" alt="OpenClaw Skill" />
  <img src="https://img.shields.io/badge/QClaw-Skill-6C5CE7?style=for-the-badge" alt="QClaw Skill" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
</p>

<h1 align="center">🚴 Bike Fit Guide</h1>
<h3 align="center">骑行姿势设定指南 · Cycling Posture & Fit Optimization</h3>

---

## 📖 Introduction · 简介

**Bike Fit Guide** is an OpenClaw / QClaw Skill that provides professional cycling bike fit guidance based on Phil Burt's *BIKE FIT* methodology. Phil Burt served as the head physiotherapist for British Cycling and Team Sky.

**Bike Fit Guide** 是一个 OpenClaw / QClaw Skill，基于菲尔·伯特（Phil Burt）《BIKE FIT：骑行姿势设定指南》提供专业的骑行姿势指导。Phil Burt 曾任英国自行车协会及天空车队首席理疗师。

> ⚠️ This is an **OpenClaw / QClaw Skill** — designed to work with AI assistants in the OpenClaw / QClaw ecosystem. It provides structured knowledge that the AI can reference during conversations about cycling posture and comfort.

---

## ✨ Features · 功能

| 功能 Feature | 说明 Description |
|-------------|-----------------|
| 🔍 **疼痛诊断** Pain Diagnosis | 按疼痛部位（脚/膝/髋/腰/颈/手/会阴）系统排查 |
| 📐 **姿势调整** Posture Adjustment | 车座高度/前后、车把、锁片设定指南 |
| 🚑 **伤病预防** Injury Prevention | 膝盖疼痛、ITBS、会阴麻木、下背痛、手麻 |
| 🧘 **柔韧性训练** Flexibility | 针对性拉伸和泡沫轴方案 |
| 📏 **参数速查** Quick Reference | 关节角度标准（Retül 动态测量） |
| ❌ **误区纠正** Myth Busting | 常见骑行姿势误区科学解析 |
| 🏎️ **车型专项** Bike-Specific | 公路车 / 计时赛 / 铁三 / 山地 / 场地 |

---

## 📦 Installation · 安装

### For OpenClaw / QClaw

```bash
# Clone or copy this skill into your skills directory
# 克隆或复制此 skill 到你的 skills 目录

# Option A: Git Clone（推荐）
git clone https://github.com/1164origami/bike-fit-guide.git ~/.qclaw/skills/bike-fit-guide

# Option B: Manual Copy（手动复制）
cp -r bike-fit-guide/ ~/.qclaw/skills/

# Option C: For OpenClaw workspace
cp -r bike-fit-guide/ <your-openclaw-workspace>/skills/
```

The AI assistant will automatically load this skill when triggered by cycling posture, bike fit, or comfort-related keywords.

当对话涉及骑行姿势、bike fit、舒适度等关键词时，AI 助手会自动加载此技能。

---

## 🗂️ Structure · 文件结构

```
bike-fit-guide/
├── SKILL.md                              # 核心技能定义 Core skill definition
├── README.md                             # 本文件 This file
├── LICENSE                               # MIT License
├── .gitignore
└── references/                           # 参考知识库 Reference knowledge base
    ├── bike-fit-parameters.md            # 参数与角度标准
    ├── common-misconceptions.md          # 常见骑行误区
    ├── dynamic_fitting.md                # 动态 Bike Fit
    ├── flexibility-and-recording.md      # 柔韧性训练
    └── injury_prevention.md              # 伤病预防与康复
```

---

## 🚀 Usage · 使用示例

When the user asks any of the following, the AI loads this skill automatically:

当用户提出以下问题时，AI 会自动加载此技能：

| 中文 | English |
|------|---------|
| "我骑车膝盖疼怎么办" | "My knee hurts when cycling" |
| "怎么调整车座高度" | "How to set saddle height" |
| "锁片应该怎么装" | "How to position cleats" |
| "骑久了手麻怎么回事" | "Why do my hands go numb" |
| "公路车应该用什么姿势" | "What posture for road cycling" |

---

## 📚 Knowledge Source · 知识来源

- **Phil Burt** — *BIKE FIT: Optimise Your Bike Position for High Performance and Injury Avoidance* (2nd Edition)
- Retül 3D dynamic fitting system standards
- UCI regulations and professional team practices

---

## 📄 License · 许可协议

MIT © [1164origami](https://github.com/1164origami)

---

<p align="center">
  <sub>Made for cyclists, by cyclists. Built for OpenClaw & QClaw.</sub>
</p>
