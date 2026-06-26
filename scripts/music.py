#!/usr/bin/env python3
"""Play / cut / resume / stop scene background music (macOS).

Usage:
  music.py play <url>   Open URL in the default browser. Switches cleanly: closes the
                        previously-played track's tab first, so calling play again does
                        not stack overlapping audio. No loop (YouTube blocks reliable
                        embed-looping) — prefer long compilations or playlist URLs for
                        sustained ambience.
  music.py switch <url> Alias for play.
  music.py cut          Instantly silence everything (mute system output). Use the instant
                        horror breaks / at a reveal.
  music.py resume       Unmute output (resume the same track).
  music.py stop         Close the current music tab and mute (end audio between scenes).

How it works: opens the raw URL directly (the approach that plays reliably). Remembers the
last URL in /tmp/coc_music_url.txt and closes tabs matching its video/playlist id before
opening a new one, so switching is clean without touching unrelated tabs. "cut" mutes system
output (the one reliable cross-app silence); play unmutes first. On non-macOS, prints the
action to do by hand.
"""
import platform
import re
import subprocess
import sys

STATE = "/tmp/coc_music_url.txt"


def is_mac():
    return platform.system() == "Darwin"


def set_muted(state):
    subprocess.run(
        ["osascript", "-e", "set volume output muted %s" % ("true" if state else "false")],
        check=False,
    )


def id_of(url):
    for pat in (r"[?&]v=([A-Za-z0-9_-]{6,})", r"youtu\.be/([A-Za-z0-9_-]{6,})",
                r"[?&]list=([A-Za-z0-9_-]+)"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return ""


def close_match(match):
    if not is_mac() or not match:
        return
    for app in ["Google Chrome", "Brave Browser", "Microsoft Edge", "Arc", "Chromium", "Vivaldi"]:
        s = ('tell application "System Events" to set r to (name of processes) contains "%s"\n'
             'if r then tell application "%s"\n'
             '  repeat with w in windows\n    repeat with t in (tabs of w)\n'
             '      try\n        if (URL of t contains "%s") then close t\n      end try\n'
             '    end repeat\n  end repeat\nend tell' % (app, app, match))
        subprocess.run(["osascript", "-e", s], check=False,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    s = ('tell application "System Events" to set r to (name of processes) contains "Safari"\n'
         'if r then tell application "Safari"\n'
         '  repeat with w in windows\n    repeat with t in (tabs of w)\n'
         '      try\n        if (URL of t contains "%s") then close t\n      end try\n'
         '    end repeat\n  end repeat\nend tell' % match)
    subprocess.run(["osascript", "-e", s], check=False,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def read_state():
    try:
        with open(STATE) as f:
            return f.read().strip()
    except OSError:
        return ""


def close_previous():
    close_match("coc_music")            # clean up any legacy embed-player tab
    prev = read_state()
    if prev:
        close_match(id_of(prev))


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    cmd = args[0]
    if cmd in ("play", "switch"):
        if len(args) < 2:
            print("%s requires a URL" % cmd); return
        url = args[1]
        close_previous()
        if is_mac():
            set_muted(False)
            subprocess.run(["open", url], check=False)
        else:
            print("PLAY:", url)
        with open(STATE, "w") as f:
            f.write(url)
    elif cmd == "cut":
        set_muted(True) if is_mac() else print("CUT MUSIC NOW")
    elif cmd == "resume":
        set_muted(False) if is_mac() else print("RESUME MUSIC")
    elif cmd == "stop":
        close_previous()
        set_muted(True) if is_mac() else print("STOP MUSIC")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
