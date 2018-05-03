# Regex objects

import re

phoneNoRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # \d stands for digit

email = 'Wow, 827-823-7429 is my phone number!!'

found = phoneNoRegEx.search(email) # Finds a match of the declared regular expression
print(found) # The whole Match object
print('Phone number found: ' + found.group()) # Returns the matched value
print()

# Grouping found matches

parenthesesRegEx = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
foundAdvanced =  parenthesesRegEx.search(email)

print(foundAdvanced.group(1)) # First group
print(foundAdvanced.group(2)) # Second
print(foundAdvanced.group(3)) # Third
print(foundAdvanced.group(0)) # Whole number, same as group()
print()

area, middle, last = foundAdvanced.groups() # declare parts of number

print(area)
print(middle)
print(last)
print()





