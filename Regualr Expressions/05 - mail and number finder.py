# Find numbers an emailadresses

import pyperclip  # Getting text from clipboard
import re # Regular expressions

# print(pyperclip.paste())

def findPhoneMail():
    
    clipboard = str(pyperclip.paste())

    
    phoneReg = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE) # Phone numbers with possible extension

    
    mailReg = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z09.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

    
    foundMatches = []
    for items in phoneReg.findall(clipboard):
        number = '-'.join([items[1], items[3], items[5]])
        if items[8] != '':
            number += ' x' + items[8]
        foundMatches.append(number)

    for items in mailReg.findall(clipboard):
        foundMatches.append(items[0])

    if len(foundMatches) > 0:
        pyperclip.copy('\n'.join(foundMatches))
        print('These are the phone numbers and email adresses found: (also copied to clipboard)')
        print('\n'.join(foundMatches))
    else:
        print('No phone numers or email adresses found')



# Test it!
# email: https://www.randomlists.com/email-addresses
# phone numbers: https://fakenumber.org/us/concord
findPhoneMail()
