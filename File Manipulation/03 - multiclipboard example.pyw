# Multiclipboard

import sys, pyperclip, shelve

clipShelf = shelve.open('multi\\mlb')



if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    clipShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(clipShelf.keys())))
    elif sys.argv[1] in clipShelf:
        pyperclip.copy(clipShelf[sys.argv[1]])



clipShelf.close()

