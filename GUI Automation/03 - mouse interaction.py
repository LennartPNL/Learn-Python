# Controlling the mouse

# CLICKING #

import pyautogui, time, random

time.sleep(2)

x, y = pyautogui.position()

# Right clicks at he position you have your cursor at that moment
pyautogui.click(x, y, button='right')
time.sleep(0.4)
pyautogui.click(x-10, y-10, button='left')

# DRAGGING #

# This will be a less elaborate retarded Picasso than i made in the image manipulation chapter
# This unicellular Picasso can only use Paint and such programs

# Gives you a bit of time to open Paint or some other drawing program
time.sleep(3)

# Focus on the window
pyautogui.click()

distance = 500

# Open up a large paint canvas before this starts, i'm not responsible if unicellular Picasso pranks you

while distance > 0:
    xPos, yPos = pyautogui.position()
    if yPos > 200 and yPos < 1000 and xPos > 10 and xPos < 1910:
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)
        duration = random.randint(0, 4)
        pyautogui.dragRel(x, y, duration=(duration/10))
        distance -= 10
    else:
        pyautogui.moveTo(500, 900)

# His work can be seen in 'Upicas.png'

# SCROLLING #

# Scrolls 200 up
pyautogui.scroll(200)

time.sleep(0.5)

# Scrolls 200 down
pyautogui.scroll(-200)


