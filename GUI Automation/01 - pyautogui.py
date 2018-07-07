# The Pyautogui module

import pyautogui, random

# Warning: to prevent pyautogui from taking over your pc,
# and making you look at a moving cursor in horror, while being unable to do anything,
# you might want to know you can stop the automation by logging off your computer.

# Another way of making sure you have time to stop you pyautogui script, is using a pause

# This will pause the script after every pyautogui function is executed, for one second

# pyautogui.PAUSE = 1

# MOUSE CONTROL #

# This prints the resolution of your monitor
print(pyautogui.size())

width, height = pyautogui.size()

# This places the cursor on 10 random places on the screen
# The movement between the current and next coordinate takes 0.3 seconds

print("Moving to given locations")

for i in range(10):
    x = random.randint(0, width)
    y = random.randint(0, height)
    pyautogui.moveTo(x, y, duration=0.3)
    print("X: %s Y: %s" % (x, y))

print("Moving relative from location")

for i in range(10):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    print("X + %s Y + %s"  % (x, y))
    pyautogui.moveRel(x, y, duration=0.3)

# Getting the mouse's position

pos = pyautogui.position()

print("Mouse is now at: " + str(pos))

