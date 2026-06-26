# Rules reference (load on demand)

Read this the moment play enters a rules-dense situation: **combat starts**, a
**sanity loss / madness** triggers, an **opposed contest** is needed, or a player
**pushes a roll**. Do not load it for ordinary investigation — the always-on micro-rules
in `SKILL.md` (掷骰 section) cover routine single checks. Resolve fast and in fiction;
report results compactly with `scripts/roll.py`.

All values below are CoC 7e (this rulebook). For weapon damage and monster specials,
use the weapon table / module stat block, not memory.

---

## Opposed checks (对抗检定)

Use for PC-vs-PC, PC-vs-NPC active resistance, and as the standard for melee. Outside
combat, prefer a plain difficulty level; only use opposed rolls when both sides actively
strive and the drama warrants it.

- Both sides declare mutually exclusive goals, each picks a skill or characteristic
  (need not match; Keeper approves).
- Both roll d100, get a success level. **Higher success level wins.** Tie → higher
  skill/characteristic value wins; still tied → stalemate or both reroll.
- Success-level order: 大成功 > 极难 > 困难 > 常规 > 失败/大失败.
- **Opposed checks cannot be pushed.**

## Difficulty levels (难度等级)

Keeper sets difficulty by how hard the task is, against the roller's own value:
- 常规: roll ≤ value. 困难: roll ≤ ½ value. 极难: roll ≤ ⅕ value.
- Set difficulty from the situation *before* rolling; do not also stack bonus/penalty
  dice on top except as a rare special case.

**Against a living opponent**: derive difficulty from their relevant skill/attribute —
< 50 → Regular; ≥ 50 → Hard; ≥ 90 → Extreme. (Also in SKILL.md always-on layer.)

## Combined skill checks (组合技能检定)

When a task simultaneously requires two skills (e.g. a device that is both mechanical
and electrical), roll **once** and compare the single result to each skill separately.
Keeper decides in advance whether *all* must succeed or *any one* is enough.

Do not ask for two separate rolls — a single roll maintains the correct probability.
Example: Mechanical 10% and Electrical 10% → a single roll gives 10% chance of passing
both, instead of 1% if rolled separately.

## Skill level benchmarks (技能等级参考)

Use to judge whether a skill value makes sense for a character concept, and for quick
NPC stat creation:

| 技能值 | 水平 | 含义 |
|---|---|---|
| 01-05% | 新手 | 完全外行 |
| 06-19% | 初学者 | 少量知识 |
| 20-49% | 业余 | 兴趣爱好水平 |
| 50-74% | 职业 | 可凭此谋生，相当于学士 |
| 75-89% | 专家 | 硕士/博士水平 |
| 90%+ | 大师 | 该领域世界顶尖 |

A 50% skill is the professional threshold — enough to make a living from it.

## Bonus / penalty dice (奖励骰 / 惩罚骰)

Only for a **significant** advantage or disadvantage — if a factor is worth just a few
percent, ignore it (light rain = nothing; blinding downpour = penalty die). Mechanics:
- Roll one **extra tens die** alongside the normal d100. Bonus die → keep the better
  (usually lower) tens result; penalty die → keep the worse (usually higher).
- **One bonus and one penalty cancel.** Normally at most one; in extreme cases two.
- Prefer bonus/penalty dice over ad-hoc % modifiers.

## Pushing a roll (孤注一掷)

When a normal check fails, the player may push by **committing harder / a new in-fiction
approach** ("I tear the whole drawer out", "I stake my reputation on it"). Reroll once.
- A **failed pushed roll brings a real, escalated consequence** — not just "nothing
  happens." That is the price of pushing; narrate it.
- Cannot push opposed checks, combat attack/defense rolls, or sanity checks.

## Luck checks & clues (don't gate the spine)

- If an outcome depends on **environment/chance rather than the PC's action**, use a
  **Luck check**, not a skill (is a cab passing at 2am? does the shop stock the item?).
- **Never gate a critical/plot-advancing clue behind a roll.** Hand core (overt) clues
  to anyone who looks; reserve rolls for *extra* detail or hidden bonuses. Describe the
  evidence and let players infer — don't explain the conclusion.
- **Idea roll (灵感检定)** to unstick a stalled table: success → the lead resurfaces
  cleanly; failure → it surfaces but at a cost (lost time, a worse position).

---

## Combat (战斗)

Only enter the combat round once blows are committed. Surprise first if applicable.

**Surprise / first strike:** an unexpected attacker should get their hit before the
combat round (don't bury them at the bottom of DEX order). Defender may get a Listen/
Spot/Psychology check (vs attacker's Stealth) to be ready. If unready: melee can be
auto-hit (except fumble) or attacker gets a bonus die; ranged always still rolls.

**Round order:** act in **DEX order, high to low.** Each combatant gets one action on
their turn (attack, maneuver, flee, take cover, etc.).

**Attack & defense:** the attacker rolls their Fighting/Firearms skill; for melee the
**defender chooses to dodge or fight back**, resolved as an opposed check.
- **Dodge:** defender's Dodge vs attacker's Fighting; defender wins/ties → avoids.
- **Fight back:** defender's Fighting vs attacker's Fighting; whoever wins deals damage.
- **Firearms:** a target cannot "fight back" against a gun and normally cannot dodge a
  bullet except by **diving for cover** (then prone/out of position). Point-blank,
  range, and cover shift the shooter's difficulty instead.

**Outnumbered:** once a character has dodged or fought back once in a round, every
further melee attack against them that round gets a **bonus die.**

**Maneuvers (战技 — disarm, grapple, shove, knock down):** compare **Build/体格**. Per
size step the target is larger, the user takes a penalty die (max 2); 3+ steps larger →
impossible. Resolve like an attack (opposed dodge/fight-back); success applies the
effect instead of (or with) damage. A maneuver needs a concrete stated objective, not
just an action.

**Damage:** roll the weapon's damage; add **damage bonus (DB)** for relevant melee/
unarmed. A successful fight-back means the winner deals their damage.

**Major wound (重伤):** a single hit dealing **≥ half the target's max HP** is a major
wound → target makes a **CON check**; fail → knocked prone/unconscious. At **0 HP** the
character is dying — First Aid stabilizes; otherwise track the dying rules.

---

## Sanity & madness (理智与疯狂)

**Sanity check:** loss is written **X/Y** (e.g. 0/1D6). Roll 1D100 vs **current** SAN;
success → lose X, failure → lose Y. A fumbled SAN check loses the max possible. One SAN
check per *encounter*, not per monster.

**Max SAN = 99 − 克苏鲁神话技能.** When Mythos rises, drop max SAN by the same amount.

**Triggers into madness:**
- **Lose 5+ SAN in one go** → the player makes an **INT check**. *Pass* = they grasp the
  horror → **temporary insanity**. *Fail* = they repress it, no insanity this time.
  (Note: here passing INT is the *bad* outcome.)
- **Lose ≥ 1/5 of current SAN within one game-day** → **indefinite insanity** (lasts
  until treated/recovered; a game-day usually ends at safe rest).
- **SAN reaches 0** → **permanent insanity**; the PC leaves play.

Temporary insanity lasts **1D10 hours**; indefinite insanity, much longer. Both begin
with a **bout of madness (phase 1)**, then an underlying-insanity period (phase 2).

### Bout of madness — duration & control

Run the bout **per the rulebook**: during it the PC is **under Keeper control** — narrate
their mad actions (or hand the player a madness prompt to play out). Two forms:

- **即时症状 (real-time):** use when other investigators are present (or Keeper wants it
  beat-by-beat even if alone). **The bout lasts 1D10 combat rounds.** Roll **1D10 on
  Table Ⅶ** (or pick a fitting result). Most entries themselves last 1D10 rounds. This
  is the answer to "how many rounds": **1D10 rounds.**
- **总结症状 (summary):** use when the PC is alone, or everyone present goes mad at once.
  Fast-forward and narrate the aftermath; the PC is lost to madness for **1D10 hours**
  (or Keeper's call). Roll **1D10 on Table Ⅷ.** If another PC encounters them before it
  ends, hand control back and play it out.

**Table Ⅶ (即时症状, 1D10, each ~1D10 rounds):** 1 失忆 / 2 假性残疾(失明·失聪·肢体缺失感) /
3 暴力倾向(无差别攻击) / 4 偏执 / 5 人际依赖(误认重要之人) / 6 昏厥 / 7 逃避行为 /
8 竭斯底里 / 9 恐惧(roll Table Ⅸ phobia) / 10 躁狂(roll Table Ⅹ mania).

**Table Ⅷ (总结症状, 1D10, ~1D10 hours):** 1 失忆 / 2 被窃(贵重物过幸运, 其余自动失) /
3 遍体鳞伤(HP 减半, 非重伤) / 4 暴力倾向 / 5 极端信念 / 6 奔向重要之人 / 7 被收容(疯人院/牢房) /
8 逃避行为(醒来在远方) / 9 恐惧(新恐惧症, Table Ⅸ) / 10 躁狂(新躁狂症, Table Ⅹ).

A "恐惧/躁狂" result installs a new **phobia/mania** (Table Ⅸ/Ⅹ — roll d100 or Keeper
picks). After the bout, the PC enters phase-2 underlying insanity and is prone to further
bouts under stress until recovered.

**Safety override:** running the bout per RAW does **not** override the skill's Safety &
consent rules — still fade to black for sexual violence/torture, and avoid forcing
irreversible harm onto *another player's* PC without a check or consent. Within those
limits, play the madness straight.
