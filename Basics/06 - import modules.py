# Importing Modules

import random

# Let's print some random numbers:

for i in range(3):
    print(random.randint(0, 1000)) # Prints numbers between 0 and 1000

# Ending a program

import sys

# Making an infinite loop that takes input

while True:
    print('Type goodbye to close this program.')
    inp = input()
    if inp == 'goodbye':
        sys.exit()  # Exits the program
    print(inp + ' is not valid..')
