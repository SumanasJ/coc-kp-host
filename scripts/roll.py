#!/usr/bin/env python3
"""Simple dice roller for COC/KP sessions.

Usage:
  python scripts/roll.py d100
  python scripts/roll.py 1d6
  python scripts/roll.py 2d6
  python scripts/roll.py 1d4+2
  python scripts/roll.py check 55
"""
import random
import re
import sys

DICE_RE = re.compile(r"^(?:(\d*)d(\d+))(?:([+-])(\d+))?$", re.IGNORECASE)


def roll_expr(expr: str) -> tuple[str, int]:
    expr = expr.strip().lower()
    if expr.startswith("d"):
        expr = "1" + expr
    m = DICE_RE.match(expr)
    if not m:
        raise ValueError("use dice like d100, 1d6, 2d6, or 1d4+2")
    n = int(m.group(1) or 1)
    sides = int(m.group(2))
    sign = m.group(3)
    mod = int(m.group(4) or 0)
    if n < 1 or n > 100 or sides < 2 or sides > 1000:
        raise ValueError("dice out of supported range")
    rolls = [random.randint(1, sides) for _ in range(n)]
    total = sum(rolls)
    if sign == "+":
        total += mod
    elif sign == "-":
        total -= mod
    detail = f"{n}d{sides}: {rolls}"
    if sign:
        detail += f" {sign} {mod}"
    return detail, total


def success_level(roll: int, value: int) -> str:
    if roll == 1:
        return "大成功"
    if roll > value:
        if roll >= 96 and value < 50 or roll == 100:
            return "大失败"
        return "失败"
    if roll <= value // 5:
        return "极难成功"
    if roll <= value // 2:
        return "困难成功"
    return "普通成功"


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: roll.py <dice_expr> | check <value>", file=sys.stderr)
        return 2
    if argv[1].lower() == "check":
        if len(argv) != 3:
            print("usage: roll.py check <value>", file=sys.stderr)
            return 2
        value = int(argv[2])
        if value < 1 or value > 100:
            raise ValueError("check value must be 1..100")
        roll = random.randint(1, 100)
        print(f"1D100 = {roll}; {success_level(roll, value)}")
        return 0
    detail, total = roll_expr(argv[1])
    print(f"{detail}; total = {total}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
