# COC KP Host

![COC KP Host 效果截图](assets/demo-screenshot.png)

English documentation: [README.md](README.md)

COC KP Host 是一个用于 Codex/ChatGPT 的中文跑团技能，定位是让模型担任 Call of Cthulhu 风格调查恐怖短团或长团的 KP。它会处理开团设置、预设调查员卡、NPC 队友、检定与投骰、玩家可见图片/手outs，以及团内连续性记录。

目前短团已经验证表现稳定，长团仍在持续验证中。

## 亮点

- 中文 COC 风格 KP 叙事，偏克制、沉浸、调查恐怖
- 开团只问最少问题：是否自定义调查员，以及需要几个 NPC 队友
- 可自动生成完整预设调查员卡：属性、HP、MP、SAN、幸运、移动、技能、携带物、性格钩子和弱点
- NPC 队友会提供质感、情绪和有限协助，但不会替玩家解谜
- 内置投骰脚本，支持 d100 检定和常见伤害、SAN、随机表骰
- 支持在合适时机展示玩家可见图片、地图、肖像和 handout
- 默认不列选项菜单，让玩家自然行动和对话
- 会维护简洁的团内连续性：地点、时间、线索、开放路线、HP/SAN/幸运/弹药、NPC 态度等

## 玩家可见材料图

当模组里有适合玩家看到的资料时，KP 可以在调查员真正看到它的那一刻，直接把图片发到对话里。这个能力很适合线索符号、地图、NPC 肖像、剪报、信件、图表和其他 handout。

![COC KP Host 材料图示例](assets/handout-screenshot.png)

## 目录结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── demo-screenshot.png
│   ├── handout-screenshot.png
│   └── icon.svg
├── references/
│   └── gameplay_style.md
└── scripts/
    └── roll.py
```

## 安装

把本目录复制到 Codex skills 目录：

```bash
cp -R coc-kp-host ~/.codex/skills/coc-kp-host
```

安装后重启 Codex，让新 skill 被重新发现。

## 使用方式

开一个新对话，用中文提出请求，例如：

```text
开一个 COC 短团，你当 KP。我用预设调查员，带 1 个 NPC 队友。
```

如果你上传模组 PDF/DOCX 或玩家可见图片资料，它会把这些内容作为 canon；当角色在剧情里看到或收到对应资料时，再展示安全的玩家可见图片。KP 专用地图、怪物数据、房间钥匙、隐藏真相和未来剧情不会直接暴露。

## 投骰工具

内置脚本支持 d100 检定和常见骰子表达式：

```bash
python scripts/roll.py check 55
python scripts/roll.py d100
python scripts/roll.py 1d6
python scripts/roll.py 1d4+2
python scripts/roll.py 2d6
```

示例输出：

```text
1D100 = 42; 普通成功
```

## 设计取向

这个 skill 更像一个会控节奏的中文 KP，而不是规则讲解器。它会把场景停在玩家可以自然行动的地方，不主动列 1/2/3 选项；失败不会被偷偷改成成功；NPC 队友有性格、偏见和可能犯错的判断，但不会成为提示机器。

更细的 NPC 队友和信息流规则见 [references/gameplay_style.md](references/gameplay_style.md)。

## 当前状态

- 短团：已经验证，表现稳定
- 长团：验证中
- 玩家可见图片/handout：已支持
- 工具调用和投骰：已通过 `scripts/roll.py` 验证

## 许可证

MIT，见 [LICENSE](LICENSE)。
