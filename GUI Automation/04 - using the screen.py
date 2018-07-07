# Clicking stuff based on what is on the screen

import pyautogui, random


pic = pyautogui.screenshot()

xSize, ySize = pyautogui.size()

i = 0

# returns the color of some random pixels

while i < 25:
    x = random.randint(0, xSize-1)
    y = random.randint(0, ySize-1)
    color = pic.getpixel((x, y))
    print("Color of pixel x: %s y: %s is: %s" % (x,y,color))
    i += 1

# MATCHING COLORS #

# True (in my case)
print(pyautogui.pixelMatchesColor(14, 97, (45,47,48)))

# False (in my case)
print(pyautogui.pixelMatchesColor(14, 97, (45,47,43)))

