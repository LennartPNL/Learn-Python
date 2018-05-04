# Reading and Writing files

import os

# Using the open() function

openFile = open('example.txt') # opens the file

print(openFile.read()) # reads all content inside the file

print(openFile.readlines()) # Puts every line as an item into a list (you might have to comment the previous print)

openFile.close() # closing the file

openFile2 = open('example2.txt', 'w') # Open it it write mode, which overwrites the whole file

openFile2.write('I just opened this file in write mode and now everything is gone\n')

openFile2.close()

openFile2 = open('example2.txt', 'a') # opens the file in append mode

openFile2.write('But now i can safely add stuff without losing all my progress')

openFile2.close()

openFile2 = open('example2.txt')

contentOfFile = openFile2.read() # write the content of the file to a variable

openFile2.close()

print(contentOfFile)
print()

# Save variables

import shelve

shelfFile = shelve.open('data')

stuff = ['Harry', 'Hagrid', 'Hermoine']

shelfFile['stuff'] = stuff # creates 3 files (bak, dat, dir) where the stuff variable is stored

shelfFile.close()

shelfFile = shelve.open('data') # Check if the data is correctly stored
type(shelfFile)
print(shelfFile['stuff'])
print()
print(list(shelfFile.keys())) # all the keys in the file
print()
print(list(shelfFile.values())) # all of the values
shelfFile.close()
print()

# Variable saving with pprint.pformat()

import pprint

foodILike = [{'name': 'curry', 'color': 'green'},{'name': 'spaghetti', 'color': 'red'},{'name': 'cheese', 'color': 'yellow'}]
print(pprint.pformat(foodILike))

varFile = open('vars.py', 'w') # creates the vars.py file, which you can import in another .py file like: import vars

varFile.write('food = ' + pprint.pformat(foodILike) + '\n') # declares the variable food in the new file

varFile.close()









