# This program brute forces encrypted PDF files that are protected with a single English word
# The word must be all lower case
# The word must be in the English dictionary

import PyPDF2
import datetime

start = datetime.datetime.now()

# The encrypted file we want to work with
encrReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# The dictionary of English words
dictionary = open('dictionary.txt', 'r')

dicList = []

# making a list from the dictionary
for word in dictionary:
    dicList.append(word.lower())

print('Get yourself a coffee because this might take a while....')

check = 0
tries = 1
# Trying every word in the dictionary as possible password
for word in dicList:
    print("Trying: " + word + "..")
    try:
        # If the password is correct
        if encrReader.decrypt(word.strip()) == 1:
            print("=====BRUTE FORCE SUCCESSFUL!=====")
            print('Password is: ' + word)
            print("Tried %s words before finding the password" % (str(tries)))
            print("It took %s to find the password" % (str(datetime.datetime.now()-start)))
            print()
            print("=====PAGE CONTENTS:=====")
            check = 1
            # Print all the page contents
            print("This document has %s pages." % (str(encrReader.numPages)))
    except Exception as e:
        print(e)
    if check == 1:
        break
    tries = tries + 1





