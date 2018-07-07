# Live tracking of your mouse's location and the color of the pixel on that location
# Works in Command Prompt and when you double click this file

import pyautogui

print("Ctrl+C quits the program")

try:
    while True:
        x, y  = pyautogui.position()
        pixColor = pyautogui.screenshot().getpixel((x,y))
        pos = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        pos += " RGB is ( %s, %s, %s )" % (str(pixColor[0]).rjust(3), str(pixColor[1]).rjust(3), str(pixColor[2]).rjust(3))
        print(pos, end='')
        print('\b' * len(pos), end='', flush=True)
except KeyboardInterrupt:
    print('\n\nReady...')
