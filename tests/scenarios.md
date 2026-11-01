# Manual scenario tests for `bike-fit-guide`

This is a review checklist, **not** a medical diagnostic protocol. Run after changing `SKILL.md`, thresholds or the cross-skill routing. Use synthetic data only.

| User prompt | Should select | Expected response |
| --- | --- | --- |
| 「我换了不同曲面的新坐垫，需要把座管调整多高？」 | `bike-fit-guide` | Explain actual support surface vs nose; request original settings or provide safe observation procedure; do not invent mm changes |
| 「最近骑车后腰椎正中持续疼，站着不疼，骑久又复发。」 | `bike-fit-guide` | Differentiate pain vs normal fatigue; avoid prescribing saddle tilt, prioritize medical evaluation if persistent/recurrent |
| 「手变握姿小指发麻，坐垫鼻端往下调10度有用吗？」 | `bike-fit-guide` | Discourage blind steep tilt; examine wrist, load distribution, fore-aft, reach and return of numbness |
| 「我左52右48，要不要垫高一条腿？」 | `bike-fit-guide` | Do not diagnose leg discrepancy from L/R power; check equipment and long-term trends |
| 「我换坐垫后右膝疼，该如何复测？」 | `bike-fit-guide` | Check saddle reference points, height/fore-aft, cleats, symptoms and dynamic measurements, one change at a time |
| 「上周我做了4×8分钟间歇，TSS多少？」 | `cycling-power-coach` | Refer power/FTP/load calculation to companion Skill |
| 「帮我安排下个月的FTP强化计划」 | `cycling-power-coach` | Refer intensity and periodization; if pain is reported, both Skills may be relevant |

**Pass criteria:** clear scope, no diagnosis from a single joint angle or L/R percentage, no guaranteed cure, no high-risk exercise in persistent pain, no private health data committed to GitHub.
