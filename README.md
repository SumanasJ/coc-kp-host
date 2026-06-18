# COC KP Host

![COC KP Host demo](assets/demo-screenshot.png)

中文说明见 [README.zh-CN.md](README.zh-CN.md).

COC KP Host is a Codex/ChatGPT skill for running Chinese Call of Cthulhu-style solo or co-op investigative tabletop RPG sessions. It acts as a Keeper, creates compact investigator sheets, manages NPC teammates, adjudicates dice checks, presents player-facing handouts when available, and keeps the pacing focused on immersive play.

The skill has been tested in short scenarios and is currently being tested in longer campaigns.

## Highlights

- Chinese-language KP narration for Call of Cthulhu-style investigative horror
- Minimal setup: custom or preset investigator, plus desired NPC teammate count
- Preset investigator card generation with attributes, HP, MP, SAN, Luck, Move, possessions, hooks, and vulnerabilities
- NPC teammates that add texture without solving the mystery for the player
- Built-in dice helper for d100 checks and common damage/SAN/random dice
- Player-facing image and handout handling for uploaded scenarios
- Grounded pacing: no option menus unless the player asks for suggestions
- Continuity tracking for clues, location, time, NPC attitudes, HP, SAN, Luck, and ammo

## Player-Facing Handouts

When a scenario includes safe player-facing material, the KP can send images directly in the conversation at the moment the investigators encounter them. This works well for clue symbols, maps, portraits, newspaper clippings, letters, diagrams, and other handouts.

![COC KP Host handout example](assets/handout-screenshot.png)

## Repository Layout

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

## Installation

Copy this directory into your Codex skills directory:

```bash
cp -R coc-kp-host ~/.codex/skills/coc-kp-host
```

Restart Codex after installing so the new skill can be discovered.

## Usage

Start a new chat and ask in Chinese, for example:

```text
开一个 COC 短团，你当 KP。我用预设调查员，带 1 个 NPC 队友。
```

The skill should ask only the minimum setup questions if needed, then start play. If you provide a scenario PDF/DOCX or player-facing handouts, it will use them as canon and present safe player-facing images at the right moment.

## Dice Helper

The included dice script supports percentile checks and common dice expressions:

```bash
python scripts/roll.py check 55
python scripts/roll.py d100
python scripts/roll.py 1d6
python scripts/roll.py 1d4+2
python scripts/roll.py 2d6
```

Example output:

```text
1D100 = 42; 普通成功
```

## Design Notes

This skill is tuned for immersive investigation rather than rules lectures. It avoids listing menu options by default, keeps Keeper-only information hidden, lets failures produce real consequences, and treats NPC teammates as fallible companions rather than hint dispensers.

For more detailed NPC teammate and information-flow guidance, see [references/gameplay_style.md](references/gameplay_style.md).

## Status

- Short scenarios: validated and stable in local play
- Longer campaigns: in progress
- Image handouts: supported when safe player-facing material is available
- Dice/tool activity: tested with the included `scripts/roll.py`

## License

MIT. See [LICENSE](LICENSE).
