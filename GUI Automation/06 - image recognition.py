# Recognize parts of your screen

import pyautogui

located = list(pyautogui.locateAllOnScreen('hiddenicons.png'))

for l in located:
    # prints a list of all found matches
    # like this (x-coordinate of left edge, y-coordinate of top edge, width, height)
    print("Hidden icons button windows at: " + str(l))

located2 = list(pyautogui.locateAllOnScreen('pyfile.png'))

if len(located2) != 0:
    for l in located2:
        print("Python file at: " + str(l))
else:
    print("No python files found on your screen")

# Clicking found stuff

for l in located:
    location = l
    # Get the center of the found item
    centerOfItem = pyautogui.center(l)
    # Clicking in the center of the found item
    pyautogui.click(centerOfItem)