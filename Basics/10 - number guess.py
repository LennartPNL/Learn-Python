# Number Guesser

import random

mysteryNum = random.randint(1, 15)
print('I have a number in mind, which is between 1 and 15')

# Guess four times

for guessed in range(1, 5):
    print('Try a number: ')
    guess = int(input())

    if guess < mysteryNum:
        print('You are thinking too low.')
    elif guess > mysteryNum:
        print('That is too high')
    else:
        # If the guessed number is neither higher nor lower, it must be the same
        break # So break out of the loop

if guess == mysteryNum:
    print('Correct, and in only '  + str(guessed) + ' guesses..')
else:
    print('You could not even guess it was ' + str(mysteryNum) + '....')
        
    
