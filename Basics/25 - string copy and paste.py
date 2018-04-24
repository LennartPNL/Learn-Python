# Copy and paste from clipboard

import pyperclip

# Pyperclip might not work for yo!
# To fix this open cmd and cd into your pytho Scripts folder
# in my case: cd C:\Python36\Scripts
# Now type 'pip install pyperclip' and hit enter
# Now it should work

someText = 'Yaya Toure'
pyperclip.copy(someText)
print(pyperclip.paste())
