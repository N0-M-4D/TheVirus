import time
import pydirectinput
import pygetwindow as gw

INTERVAL = 120          # seconds between moves
KEYS = ["w", "a", "s", "d"]
HOLD_EACH = 1.25        # seconds to hold each key (4 x 1.25 = 5 seconds total)

pydirectinput.FAILSAFE = False

def focus_roblox():
    wins = [w for w in gw.getWindowsWithTitle("Roblox") if w.title.strip() == "Roblox"]
    if not wins:
        return False
    try:
        if wins[0].isMinimized:
            wins[0].restore()
        wins[0].activate()
    except Exception:
        pass
    time.sleep(0.5)
    return True

print("Anti-AFK running. Switch to Roblox. Ctrl+C to stop.")
time.sleep(5)
while True:
    if focus_roblox():
        print(time.strftime("[%H:%M:%S]"), "Moving W A S D...")
        for key in KEYS:
            pydirectinput.keyDown(key)
            time.sleep(HOLD_EACH)
            pydirectinput.keyUp(key)
    else:
        print(time.strftime("[%H:%M:%S]"), "Roblox window not found, skipping.")
    time.sleep(INTERVAL)
