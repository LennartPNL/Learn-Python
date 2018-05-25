# Using the webbrowser module

import webbrowser

# Opens a browser tab with the given URL
webbrowser.open('www.paypal.me/dikdik')

# Finding adresses on Google maps

import sys, pyperclip

if len(sys.argv) > 1:
    # Checks if command arguments have been added
    address = ' '.join(sys.argv[1:])
else:
    # If no commands are typed, the program will use whatever is on your clipboard
    address = pyperclip.paste()


    
webbrowser.open('www.google.com/maps/place/' + address)

