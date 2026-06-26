# COC KP Host

Chinese main README: [README.md](README.md)

A Chinese Call of Cthulhu-style Keeper skill for Claude Code, Codex, and ChatGPT. It lets the model run investigative horror one-shots or longer campaigns as a Keeper: player briefing, preset investigator cards, NPC teammates, checks and dice, scenario preparation, player-facing handouts, scene music, and continuity records across sessions.

![COC KP Host demo](assets/demo-screenshot.jpg)

## What It Is For

- Run a Chinese CoC-style one-shot with the model as Keeper
- Upload a PDF/DOCX scenario and let the Keeper prepare it privately, then run it from canon
- Generate playable preset investigators and NPC teammates
- Show player-facing images, maps, clippings, letters, and handouts only when characters actually encounter them
- Score scenes with music and cut to silence at horror reveals
- Track clues, location, time, HP/SAN/Luck, NPC attitudes, and session transcripts for later continuation

## Latest Highlights

### 1. A More Table-Like Chinese Keeper

The default language is Simplified Chinese, with a restrained, immersive investigative-horror tone. It does not start by listing menus or pushing players into 1/2/3 choices. Instead, it uses short scenes, NPC reactions, clues, and pressure to stop at the moment where the player can naturally act.

When starting a new scenario, it asks only the minimum setup questions:

1. Do you want a custom investigator, or a preset card?
2. How many NPC teammates do you want?

If you say "start immediately", it uses sensible defaults and begins play.

### 2. Scenario Prep With Spoiler Control

When you provide a PDF, DOCX, image pack, or other scenario material, the Keeper first performs a private preparation pass:

- Extract or inspect scenario text and build a Keeper-facing scene index
- Organize major locations, NPCs, timelines, clue gates, danger zones, and ending conditions
- Separate player-facing materials from Keeper-only information
- Hide monster stats, room keys, future events, hidden truths, and solution routes
- Before entering a key location, NPC, clue, or event, search the scenario text first and then narrate from canon

The goal is not to publicly summarize the module. The goal is for the Keeper to know the table, while the player only sees what their character can see.

### 3. Player-Facing Images and Handouts

If a module includes player-safe images, maps, portraits, clippings, letters, symbols, or diagrams, the Keeper presents them at the exact moment the investigator encounters them.

![COC KP Host handout example](assets/handout-map-preview.jpg)

Text handouts are not exposed as mechanical labels like "Handout 1" or "Player Material 2". They are reframed as in-world objects:

- "The note says..."
- "The clipping's edges have yellowed; beneath the headline are a few lines..."
- "The type on the archive page is faint..."
- "On the back of the photograph is a line written in pencil..."

If an image mixes player-facing and Keeper-only information, the Keeper crops or recreates only the safe part, or describes it instead of exposing the whole image.

### 4. Scene Music Control

Music is not just decoration. This skill treats soundtrack playback as an operational table tool: during prep it prepares cue links for different scene moods, and during play it can start, switch, cut, or resume audio so sound supports pacing instead of being tied to one specific module.

During prep, the Keeper builds a general-purpose music cue sheet, for example:

| Scene mood | Music strategy |
| --- | --- |
| Arrival / social | bright, lively, period-appropriate |
| Investigation | low, uneasy, loopable |
| Ritual / mourning | solemn, slow, oppressive |
| Chase / crisis | urgent, tense, driving |
| Horror reveal | hard silence, leaving a deliberate pause |

Included script:

```bash
python scripts/music.py play <url>     # open a track and unmute
python scripts/music.py switch <url>   # switch tracks without stacking audio
python scripts/music.py cut            # instantly silence everything
python scripts/music.py resume         # resume sound
python scripts/music.py stop           # stop music and close the current music tab
```

Music control currently targets macOS. On other platforms it degrades gracefully by printing what the user should do manually. The README no longer uses a single module-specific music diagram, because this feature is better presented as a general play / switch / cut / resume tool.

### 5. NPC Teammates, Full-PC Control, and Split Parties

By default, NPC teammates are not hint machines or Keeper mouthpieces. They are investigators who can be wrong, biased, emotional, and capable of their own checks. They add texture and skill coverage, but they do not solve the mystery for the player or reveal Keeper-only information.

You can also switch to "player controls all PCs":

- The player voices and decides for every PC
- The Keeper owns scene framing, pacing, NPC reactions, dice, and spotlight
- Each beat names the exact PC the moment calls on

The skill also supports splitting the party. Each group keeps its own location, time, and clues; the Keeper cuts between threads at natural beats, and information does not leak between groups until characters regroup and share it in-world.

### 6. CoC 7e-Style Checks and Quick Reference

The included `scripts/roll.py` handles common dice rolls:

```bash
python scripts/roll.py check 55
python scripts/roll.py d100
python scripts/roll.py 1d6
python scripts/roll.py 1d4+2
python scripts/roll.py 2d6
```

Supported table behavior includes:

- Regular / hard / extreme success
- Bonus and penalty dice principles
- SAN loss
- Pushed rolls
- Quick reference for rules-dense moments such as combat, madness, and opposed checks

Luck spending is disabled by default unless the player explicitly asks to enable it.

### 7. Investigator Cards and Carry Audit

Preset investigators include:

- Basic identity, age, occupation, education, residence, and hometown
- STR, CON, SIZ, DEX, APP, INT, POW, EDU, and Luck
- HP, MP, SAN, Move, damage bonus/build
- 10-14 relevant skills
- Credit Rating and lifestyle
- Key carried items
- Appearance, growth background, beliefs, important person/place/item, and vulnerabilities or secrets
- One Key Background Connection marked with a star

When a player claims to carry a valuable, rare, restricted, illegal, or combat-relevant item, the Keeper audits it by era, source, affordability, legality, and occupation. Implausible items are not granted for free; they are marked as "must be acquired in play".

## Repository Layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── demo-screenshot.jpg
│   ├── demo-screenshot.png
│   ├── handout-map-preview.jpg
│   ├── handout-screenshot.png
│   ├── icon.svg
├── references/
│   ├── carry_audit.md         # carry and purchase plausibility audit
│   ├── gameplay_style.md      # NPC teammate and information-flow rules
│   ├── prep_persistence.md    # durable prep, handout indexes, music indexes, logs
│   └── rules_reference.md     # CoC 7e-style quick reference
└── scripts/
    ├── music.py               # scene music control
    └── roll.py                # dice helper
```

## Installation

Copy this directory into the relevant host's skills folder:

```bash
# Claude Code
cp -R coc-kp-host ~/.claude/skills/coc-kp-host

# Codex
cp -R coc-kp-host ~/.codex/skills/coc-kp-host
```

After installing or updating, restart the host app so the skill can be rediscovered.

## Usage

The most direct flow is to upload the scenario file, then type:

```text
/coc-kp-host
```

You can also trigger it with natural language, for example:

```text
我上传了一个 COC 模组。请你用 coc-kp-host 当 KP，先私下备团，不要剧透。
我想用预设调查员，带 1 个 NPC 队友；玩家看到图片或讲义时再展示给我。
```

If you do not upload a scenario, you can also start an original one-shot:

```text
开一个 COC 短团，你当 KP。我用预设调查员，带 1 个 NPC 队友。
```

## Design Direction

This skill aims to be a Chinese Keeper who controls pacing, not a rules explainer. It tries to:

- Preserve player agency
- Turn failure into consequences instead of secretly converting it to success
- Give NPC teammates personality without letting them steal the mystery
- Use images and music for immersion, not spoilers
- Keep each scene grounded in module canon
- Record long-running campaign state so play can resume later

## Current Status

- One-shots: validated
- Full modules: validated end to end
- PDF/DOCX scenario prep: supported
- Player-facing images/handouts: supported
- Scene music: supported on macOS, graceful manual fallback elsewhere
- CoC-style dice: supported
- Persistent logs: supports state logs and near-verbatim narrative transcripts

## License

MIT. See [LICENSE](LICENSE).
