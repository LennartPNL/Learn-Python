# The While Loop


monty = 0
python = 10

# While the value of monty is smaller than python's value
# everything within the loop will be executed

while monty < python:   
    print('Currently at: ' + str(monty))
    # Python does not allow the increment operator: monty++ won't work
    monty += 1


# A loop that causes angry users:

name = ''

while name != 'ur name m8':
    print('pls type ur name m8')
    name = input()
print('good job')


# Break statements in loops:

nameTwo = ''

while True: # Enter a infinite loop, the condition is always True
    print('pls type ur name m8')
    nameTwo = input()
    if nameTwo == 'ur name m8':
        break   # Stops the loop from running
print('nicely done')

# Continue statements in loops:

nameThree = ''

while True: # Enter a infinite loop, the condition is always True
    print('Wots ur name m8?')
    nameThree = input()
    if nameThree != 'piraato':
       continue # If any other name than piraato is entered, the program will jump back to the start of the loop
    print('Hey there, piraato! Enter your password (it might be an animal)')
    password = input()
    if password == 'dikdik':
        break # When dikdik is entered, the program jumps out of the while loop
print('You are logged in, hackerman.')
    
