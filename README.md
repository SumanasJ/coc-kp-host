# COC KP Host

![COC KP Host demo](assets/demo-screenshot.png)

中文说明见 [README.zh-CN.md](README.zh-CN.md).

COC KP Host is a skill for running Chinese Call of Cthulhu-style solo or co-op investigative tabletop RPG sessions (works as a Claude Code / Codex / ChatGPT skill). It acts as a Keeper: it briefs the table, creates compact investigator sheets, manages NPC teammates, adjudicates dice, **scores the scene with period-appropriate music**, **shows player-facing images and handouts at the right moment**, and keeps the pacing focused on immersive play.

The skill has been tested in short scenarios and full-length published modules (e.g. the *Dead Man's Stomp* starter).

## Highlights

- Chinese-language KP narration for Call of Cthulhu-style investigative horror
- Minimal setup: custom or preset investigator, plus desired NPC teammate count
- Preset investigator cards with attributes, HP/MP/SAN/Luck/Move, possessions, hooks, and vulnerabilities
- 🎵 **Diegetic music engine** — cues, switches, and hard-cuts period soundtracks at the right beats *(new)*
- 🖼️ **Player-facing image & handout handling** — auto-extracts art from uploaded PDFs/DOCX and shows the safe ones in-scene *(improved)*
- 🎭 **Configurable control mode** — let the player run *all* PCs while the KP drives pacing/spotlight, with full party-split support *(new)*
- Built-in dice helper for d100 checks and common damage/SAN/random dice
- Grounded pacing: no option menus unless the player asks for suggestions
- Continuity tracking for clues, location, time, NPC attitudes, HP, SAN, Luck, and ammo

## 🎵 Diegetic Music (new)

When a setting leans on music — 1920s jazz, a cursed record, a funeral hymn — the KP treats it as a **live element of the scene** instead of flavor text.

During prep, the Keeper builds a small **music cue sheet** that maps each scene mood to a ready-to-play track:

| Scene mood | Example track |
| --- | --- |
| Arrival / social | upbeat hot jazz |
| Investigation | slow blues |
| Funeral / ritual | New Orleans dirge (loopable playlist) |
| Horror reveal | — silence — |

In play, `scripts/music.py` drives playback and — critically — **cuts the music the instant horror breaks**. Silence at the reveal is part of the scare.

```bash
python scripts/music.py play <url>     # open a track and unmute (switches cleanly, no overlap)
python scripts/music.py switch <url>   # alias for play
python scripts/music.py cut            # instantly silence everything (use at the reveal)
python scripts/music.py resume         # unmute / resume the same track
python scripts/music.py stop           # close the music tab and mute between scenes
```

How it works: it opens the track in your default browser and uses system-output mute as the one reliable cross-app "cut", remembering the last URL so switching tracks never stacks overlapping audio. **macOS only** for now (uses `osascript`/`open`); on other platforms it prints the action to do by hand. Prefer long compilations or playlist URLs for loopable ambience.

> Module-aware twist: when a scenario makes *relentless cheerful music itself* the source of dread (e.g. a band that keeps swinging straight through a murder), the KP keeps it playing and cuts only at the uncanny reveal.

## 🖼️ Player-Facing Handouts & Images

When a scenario includes safe player-facing material, the KP sends images **directly in the conversation at the moment the investigators encounter them** — clue symbols, maps, portraits, newspaper clippings, letters, diagrams, and other handouts.

![COC KP Host handout example](assets/handout-screenshot.png)

For uploaded **PDF/DOCX** scenarios, the Keeper extracts embedded artwork during prep, builds a private spoiler-safe contact sheet/index, and only surfaces the player-facing pieces — Keeper-only maps, stat blocks, and room keys stay hidden. Text handouts are reframed as in-world objects ("便笺上写着……", "剪报边缘已经发黄……") rather than mechanical labels.

## 🎭 Control Mode & Party Splits (new)

Two table styles, switchable mid-session:

- **AI-played teammates (default):** NPC companions act as fallible investigators — banter, instincts, and their own checks — but never solve the mystery for the player.
- **Player controls all PCs:** you voice and decide for every PC including teammates; the KP keeps owning scene framing, pacing, NPC reactions, dice, and the **spotlight** — narrating the situation, then cueing exactly which PC the moment calls on.

Both modes support **splitting the party**: each thread runs as its own short scene, the KP cuts between them, tracks each group's separate location/time/clues, and never leaks what one group learned into another until they regroup in-world.

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
│   ├── gameplay_style.md      # NPC teammate & information-flow rules
│   ├── prep_persistence.md    # durable prep folders, cards, handout/music indexes, logs
│   ├── rules_reference.md     # CoC-style adjudication quick reference
│   └── carry_audit.md         # equipment / possessions plausibility audit
└── scripts/
    ├── roll.py                # dice helper
    └── music.py               # scene music: play / switch / cut / resume / stop
```

## Installation

Copy this directory into your skills directory:

```bash
# Claude Code
cp -R coc-kp-host ~/.claude/skills/coc-kp-host
# Codex
cp -R coc-kp-host ~/.codex/skills/coc-kp-host
```

Restart the host app after installing so the new skill can be discovered.

## Usage

Start a new chat and ask in Chinese, for example:

```text
开一个 COC 短团，你当 KP。我用预设调查员，带 1 个 NPC 队友。
环境允许的话，请配上应景的音乐。
```

The skill asks only the minimum setup questions, then starts play. If you provide a scenario PDF/DOCX or player-facing handouts, it uses them as canon, presents safe player-facing images at the right moment, and cues music to match each scene.

## Dice Helper

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

This skill is tuned for immersive investigation rather than rules lectures. It avoids menu options by default, keeps Keeper-only information hidden, lets failures produce real consequences, treats NPC teammates as fallible companions, and uses sound and imagery to pull the player into the scene — never to spoil it.

For deeper NPC teammate and information-flow guidance, see [references/gameplay_style.md](references/gameplay_style.md); for durable prep folders, character cards, handout/music indexes, and session logs, see [references/prep_persistence.md](references/prep_persistence.md).

## Status

- Short scenarios: validated and stable in local play
- Full-length modules: validated end-to-end (e.g. *Dead Man's Stomp*)
- Image handouts: supported when safe player-facing material is available
- Scene music: supported on macOS via `scripts/music.py` (graceful no-op elsewhere)
- Dice/tool activity: tested with the included `scripts/roll.py`

## License

MIT. See [LICENSE](LICENSE).
