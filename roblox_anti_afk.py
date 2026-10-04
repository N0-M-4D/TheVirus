"""
Roblox anti-AFK: holds W for 5 seconds every 2 minutes.

Setup (Windows):
    pip install pydirectinput pygetwindow

Usage:
    1. Open Roblox and join your game.
    2. Run:  python roblox_anti_afk.py
    3. Press Ctrl+C in this terminal to stop.

The script brings the Roblox window to the front before pressing W,
so you can use other windows in between (it will steal focus briefly).
"""

import time

import pydirectinput  # Roblox ignores normal virtual keys; this sends DirectInput scan codes

try:
    import pygetwindow as gw
except ImportError:
    gw = None

INTERVAL_SECONDS = 120  # time between presses
HOLD_SECONDS = 5        # how long to hold W
KEY = "w"

pydirectinput.FAILSAFE = False


def focus_roblox():
    """Bring the Roblox window to the front. Returns True if found."""
    if gw is None:
        return True  # can't check; assume Roblox is already focused
    windows = [w for w in gw.getWindowsWithTitle("Roblox") if w.title.strip() == "Roblox"]
    if not windows:
        return False
    win = windows[0]
    try:
        if win.isMinimized:
            win.restore()
        win.activate()
    except Exception:
        pass  # activate() can throw even when it worked
    time.sleep(0.5)
    return True


def press_w():
    pydirectinput.keyDown(KEY)
    time.sleep(HOLD_SECONDS)
    pydirectinput.keyUp(KEY)


def main():
    print(f"Anti-AFK running: holding '{KEY.upper()}' for {HOLD_SECONDS}s every {INTERVAL_SECONDS}s.")
    print("Starting in 5 seconds... (Ctrl+C to stop)")
    time.sleep(5)
    try:
        while True:
            if focus_roblox():
                print(time.strftime("[%H:%M:%S]"), f"Holding {KEY.upper()}...")
                press_w()
            else:
                print(time.strftime("[%H:%M:%S]"), "Roblox window not found, skipping.")
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        pydirectinput.keyUp(KEY)
        print("\nStopped.")


if __name__ == "__main__":
    main()
