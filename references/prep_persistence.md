# Prep persistence notes

Use these notes when a CoC session has a provided scenario file, a continuing campaign, multiple NPC teammates, strict character-card requirements, or the user asks to store prep outside chat memory.

## Create a campaign prep folder

When a writable workspace is available, create a durable project folder before or during prep. Prefer the workspace root unless the user specifies another location.

Recommended structure:

```text
KP_host/<scenario-name>/
├── README.md
├── 00_守秘人资料/
│   └── 备团索引.md
│   └── 模组框架.md
├── 01_模组原文/
│   ├── <scenario>.docx|pdf|txt
│   └── <scenario>.txt
├── 02_玩家资料/
│   └── handouts/
├── 03_角色卡/
│   ├── 调查员_<name>.md
│   └── NPC队友_<name>.md
├── 04_跑团记录/
│   └── session_log.md
└── 05_规则与流程/
    └── 车卡与跑团格式.md
    └── 文风参考.md
```

Keep player-facing and Keeper-only materials separate. Never expose `00_守秘人资料/` or full `01_模组原文/` content to the player unless that content is explicitly player-facing.

## Populate the folder

- Copy the original scenario file into `01_模组原文/`.
- Extract text to `01_模组原文/<scenario>.txt` when possible for fast search.
- Extract player-facing images/maps/handouts into `02_玩家资料/handouts/`; create an index in `00_守秘人资料/备团索引.md`.
- Create `00_守秘人资料/模组框架.md` with a spoiler-safe-for-KP framework: major locations, NPCs, timeline/day events, clue gates, handouts, night/dream triggers, hazards, and likely endings. This is a private guardrail, not a player summary.
- Create `05_规则与流程/文风参考.md` when scenario text is available. Record compact, spoiler-safe player-facing style samples or paraphrases for opening tone, location texture, document/object framing, and NPC dialogue cadence.
- Write strict character cards into `03_角色卡/` instead of leaving them only in chat.
- Write current state and stop point into `04_跑团记录/session_log.md` after each meaningful scene.
- Write local card requirements and running conventions into `05_规则与流程/车卡与跑团格式.md`.

If the workspace is a Git repository, check `git status` and recent history before creating files. Do not stage or commit unless the user asks or the workspace instructions require it.

## Build a Keeper scenario frame

Before play, skim the extracted scenario text and create `00_守秘人资料/模组框架.md`. Keep it concise and indexed for fast return-to-canon during play:

```markdown
# 模组框架

## 核心结构
- 前日谈/开场：
- 白天现实探索：
- 夜晚/梦境/异世界触发：
- 结局或大分支：

## 地点索引
- <地点名>：原文关键词；可见信息；隐藏信息；相关 NPC；危险；可获得线索。

## NPC 索引
- <NPC>：公开身份；出现位置/时间；立即目标；压力/恐惧；对调查员态度；说话风格；知道什么；不会说什么；相关支线；示例台词。

## 时间线/事件
- Day 1：
- Day 2：
- Day 3：
- 其他触发：

## 玩家可见资料/图片
- <内部编号或名称>：玩家何时可见；场内呈现方式；文件路径。

## 文风参考
- 开场语气：
- 地点描写：
- 资料/实物呈现：
- NPC 对话：
- 玩家情绪体验：

## 回原文检索关键词
- <地点/NPC/事件>：关键词 A / 关键词 B / 旧称 / 错别字或近义词。
```

Do not expose this file to the player. Use it to keep pacing and canon aligned.

Keep Keeper-facing labels in private notes. In visible play, never call a clue "文字材料 1", "Handout 2", "玩家材料", or "boxed text". Present it as an in-world object: a folded note, clipping, ledger page, police abstract, diary entry, symbol sketch, photograph, map, or testimony.

## Build module style references

When scenario text is available, skim for player-facing prose before play and record compact style references in `05_规则与流程/文风参考.md`. Prefer passages that are safe to imitate without revealing secrets:

- Opening read-aloud or premise wording.
- Location sensory details such as smell, light, noise, paper texture, architecture, crowd, weather, and silence.
- Handout wording and object presentation, such as how a clipping, letter, diary, or official record looks in the fiction.
- NPC dialogue rhythm, social pressure, and era-specific vocabulary.
- The intended emotional ride for players: curiosity, suspicion, grounded dread, social friction, relief after discoveries, or pressure to act.

Use these references as a voice guide, not as a public quote bank. During play, adapt the style into the current scene and avoid copying Keeper instructions, section titles, labels, or future-scene structure.

## Prepare NPC performance cards

For recurring or scene-important NPCs, prepare a compact private performance card before play or before their first scene:

```markdown
## <NPC name>
- Public role:
- Scene function:
- Immediate want:
- Pressure/fear:
- Attitude to investigators:
- Speech style:
- Knows:
- Withholds/does not know:
- Emotional use:
- Sample lines:
```

Use these cards to make NPC dialogue distinct and emotionally useful. A nervous landlord, bored editor, proud archivist, frightened witness, and street gossip should not sound interchangeable. Keep sample lines spoiler-safe unless they are stored in Keeper-only notes.

## Create a spoiler-free player briefing

Before character creation, create or present a spoiler-free briefing. It may live in `05_规则与流程/开团导入.md` or the visible setup response.

Include:

- Scenario title, rule edition, era, and tone.
- Non-spoiler premise: what brings the investigator into the story.
- Recommended real player count and recommended AI PC teammate count.
- Recommended skills and why they are useful in broad terms, not exact clue gates.
- Character concept guidance: fitting occupations, emotional hooks, relationships, wounds, or reasons to investigate.
- Team coverage suggestions: one social/investigation lead, one medical/practical support, one local culture/research support, etc.
- Content notes and table preferences when relevant.

Do not include hidden truth, monster identity, exact ending conditions, scripted betrayals, future scene secrets, stat blocks, or route solutions.

## Search-before-scene rule

When the player chooses a location, NPC, clue, or keyword from a provided scenario, return to the extracted scenario text before narrating if there is any chance the scene has canon details.

Use fuzzy local search, not memory:

```bash
rg -n "关键词1|关键词2|旧称|近义词" "01_模组原文/<scenario>.txt"
sed -n '<start>,<end>p' "01_模组原文/<scenario>.txt"
```

Examples:

- Player goes to a location: search the location name, alternate names, nearby landmarks, and scene title.
- Player asks about an NPC: search the NPC name, family names, job titles, and fixed refresh/location notes.
- Player enters night/dream/rest: search dream, night,异世界, event/day triggers, and current hotel/location.
- Player inspects a document/image/object: search internal handout title, caption, media index, visible text, and the in-world object name.

After reading the passage, adapt it to the current table state:

- Preserve canon facts, NPC positions, hazards, and clue gates.
- Change surface framing only when needed to respect player choices.
- If the player created a new approach, map it onto the closest canon scene rather than inventing a disconnected scene.
- If you intentionally diverge, record the divergence and reason in `session_log.md`.

## Scene-drift audit

After each major scene, update the log with:

- Canon source used: searched terms or rough source passage.
- What was revealed.
- What remains hidden.
- Any deliberate deviation from the module.

If a session has drifted for several scenes without touching a prepared location, NPC, clue gate, night/dream trigger, or timeline event, actively offer or narratively surface the next module-relevant hook.

## Narrative steering without railroading

The KP owns pacing and scenario integrity. The player owns their character's choices. When the player wanders, jokes, delays, or follows a side idea, do not simply abandon the module spine. Use soft in-world pressure to bring the table back:

- Let time pass and advance the module timeline.
- Have prepared NPCs move, call, disappear, refuse access, request help, or create consequences.
- Surface a clue through environment, handout, dream, news, official process, or overheard talk.
- Close unproductive loops with a clear result, then point the scene toward a prepared lead.
- Use night/rest/dream triggers proactively when the module expects them.
- Let risky off-route actions produce costs or partial information rather than creating a new unrelated plot.
- Say out of character only when needed: "KP note: this seems outside the scenario spine; I can resolve it briefly and move us back."

Do not force a single solution, teleport the PC without cause, or negate reasonable player plans. Redirect through believable fiction and consequences.

## Strict investigator-card template

Use this shape for player investigators:

```markdown
# 调查员：<name>

性别：
年龄：
职业：
教育水平：
住地：
故乡：
当前时间：
信用评级：<number>，<lifestyle description>

## 简短背景故事

<coherent growth history and reason to enter the case>

## 属性

STR
CON
SIZ
DEX
APP
INT
POW
EDU
合计：

HP
MP
SAN
Luck
MOV
伤害加值，体格

## 技能

<10-14 skills with percentages, including native language when appropriate>

## 随身物品

<scenario-relevant carried items>

## 背景条目

个人描述/角色外貌：
思想与信念：
重要之人：
意义非凡之地：
宝贵之物：
特质：
难言之隐：

关键背景连接 ★：<在上述条目中选一项标注，失去时 1/1D6 SAN，守秘人不得在未给玩家骰骰机会的情况下摧毁>
```

Omit optional background entries only when they truly do not fit, not for brevity.

## NPC teammate-card template

Use this shape for recurring NPC teammates:

```markdown
# NPC 队友：<name>

性别：
年龄：
职业/当前状态：
教育水平：
住地：
故乡：
信用评级：<number>，<lifestyle description>

## 进入案件方式与关系

<how they enter the case; relationship to PC and other teammates>

## 外貌

<player-facing first impression>

## 简短背景故事

<coherent growth history, skills, beliefs, and reason to join>

## 属性

STR
CON
SIZ
DEX
APP
INT
POW
EDU
合计：

HP
MP
SAN
Luck
MOV
伤害加值，体格

## 技能

<8-12 relevant skills, including native language and Credit Rating>

## 随身物品

<items likely to matter in scenes or checks>

## 背景条目

思想与信念：
重要之人/重要之地：
宝贵之物：
特质：
弱点：
关键背景连接 ★：<选一项标注>
```

NPC teammates may exceed or fall short of PC point-buy totals, but their values should stay ordinary unless the scenario justifies otherwise.

## Session log template

Update `04_跑团记录/session_log.md` after each scene, before long pauses, and whenever HP/SAN/Luck/resources or clue state changes:

```markdown
## 当前停点

<where play should resume; include the exact last prompt or scene beat>

## 已获得线索

<player-facing clues only>

## 开放方向

<known leads the investigators can pursue>

## 状态记录

- PC: HP / SAN / Luck / notable resources
- NPC: HP / SAN / Luck / notable resources

## NPC 态度

<brief relationship and attitude notes>
```

Keep the log spoiler-safe from the player's perspective unless it is stored under `00_守秘人资料/`.
