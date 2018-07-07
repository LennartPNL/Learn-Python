# Live tracking of your mouse's location
# Works in Command Prompt and when you double click this file

import pyautogui

print("Ctrl+C quits the program")

try:
    while True:
        x, y  = pyautogui.position()
        pos = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(pos, end='')
        print('\b' * len(pos), end='', flush=True)
except KeyboardInterrupt:
    print('\n\nReady...')
