# Bike Fit Guide

基于菲尔·伯特（Phil Burt）《BIKE FIT：骑行姿势设定指南》的专业骑行姿势指导 Skill。

Phil Burt 是英国自行车协会及天空车队首席理疗师，本书是自行车 Bike Fitting 领域的权威参考。

## 功能介绍

- **骑行疼痛诊断**：按身体部位（脚/膝/髋/腰/颈/手/会阴）定位，使用 AEIOU 法排查原因
- **姿势参数参考**：车座高度/前后、车把位置、锁片设定的标准范围和调整原则
- **常见误区纠正**：主动纠正 7+ 个常见骑行误区
- **柔韧性训练**：针对性拉伸和泡沫轴训练方案
- **动态 Bike Fit**：3D 运动捕捉、气动姿势量化等进阶知识
- **伤病预防**：膝盖疼痛、ITBS、会阴麻木、下背痛、手麻等常见骑行伤病的预防和康复
- **车型专项**：公路车、计时赛、铁三、山地车等不同车型的设定差异

## 安装方法

将此 Skill 放入你的 QClaw/OpenClaw skills 目录即可。

```bash
# 克隆到 QClaw skills 目录
git clone https://github.com/1164origami/bike-fit-guide.git ~/.qclaw/skills/bike-fit-guide
```

## 使用说明

在对话中提及以下关键词即可触发：
- `bike fit` / `骑行姿势` / `车座` / `车把`
- `锁片` / `膝盖疼` / `骑行疼痛`
- `气动姿势` / `计时赛姿势`

Skill 会自动加载并提供专业建议。

## 使用示例

```
用户：我骑车膝盖前面疼，怎么办？
→ Skill 加载 bike-fit-parameters.md 诊断表
→ 定位髌骨疼痛 → 检查车座前后位置/车座高度
→ 给出 AEIOU 排查建议和调整方案
```

## 文件结构

```
bike-fit-guide/
├── SKILL.md                          # Skill 主文件
├── README.md                         # 本文件
├── LICENSE                           # MIT License
├── .gitignore
└── references/
    ├── bike-fit-parameters.md        # 关节角度标准、诊断表
    ├── common-misconceptions.md      # 常见误区与纠正
    ├── dynamic_fitting.md            # 动态 Bike Fit 进阶
    ├── flexibility-and-recording.md  # 柔韧性训练方案
    └── injury_prevention.md          # 骑行伤病预防与康复
```

## License

MIT License - 详见 [LICENSE](LICENSE)

## 参考来源

- Phil Burt, *BIKE FIT: Optimise Your Bike Position for High Performance and Injury Avoidance* (2nd Edition)
- Retül 动态 Bike Fit 系统
