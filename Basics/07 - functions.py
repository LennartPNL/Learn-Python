# Functions

def message():  #Defining a function named message
    print('What is up?')
    print('44 + 88 = ' + str(int(44+88)))
    # Everything inside this block is part of the function 

message()   # Calling the function, this executes the function

# Defining functions with parameters

def welcome(name):  # This function takes the parameter name
    print('Well hello there, ' + name)

welcome('John') # Passing John as the name variable value
welcome('Piraato')

# Return values

import random

def lifeQuestions(number):
    if number == 1:
        # When 1 is used as input, the function returns 'Most definetely.'
        return 'Most definitely.' 
    elif number == 2:
        return 'Absolutely not.'
    elif number == 3:
        return 'Questionable.'

usenum = random.randint(1,3)
answer = lifeQuestions(usenum)
print('Should i cry in bed today? ' + answer)    
