# Controlling the keyboard

import pyautogui, time

# Some time to open notepad
time.sleep(3)

pos = pyautogui.position()

# Focus on the app (notepad)
pyautogui.click(pos)

# Puts the string into notepad
pyautogui.typewrite("Hey, Python can type stuff!\n")

# KEY NAMES #

# Types BAab
pyautogui.typewrite(['a','b','left','left','B', 'A'])


# All possible keys you can pass to typewrite()
posKeys = pyautogui.KEYBOARD_KEYS

print(posKeys)

# Watch your capslock LED
for i in range(6):
    pyautogui.press('capslock')
    time.sleep(0.5)

# Windows key
for i in range(6):
    pyautogui.press('winleft')
    time.sleep(0.5)

# Muting sound
for i in range(6):
    pyautogui.press('volumemute')
    time.sleep(0.1)

# Pressing and releasing keys

# key down holds the specified key down
pyautogui.keyDown('shift')
pyautogui.typewrite("\nomg")
pyautogui.press('1')
pyautogui.press('1')
pyautogui.press('1')
# key up releases the key
pyautogui.keyUp('shift')
pyautogui.press('1')

# Hotkey combinations

pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.press('right')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite('\nI just copy pasted some stuff...')







