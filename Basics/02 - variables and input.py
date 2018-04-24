# Input exmaple and variable value assignment

print('Yo nerd, waddup?')
print('Tell me your name:')
myName = input() # Assigns whatever you type to the myName variable

print('Nice to meet you, ' + myName + '!') # Print text with a variable name
print('Your name consists of this many characters: ')

print(len(myName)) # len() counts the characters in the myName variable
print('Now then, tell me your age in years: ')
myAge = input()

# A stupid dad-joke to show how arithmetic works.
# Note the int() - This makes sure you can calculate a value
# The calculation takes place inside a str()
# - since we are trying to print a string, it should be a str()
print("Well, " + myName + "... You will be " + str(int(myAge) + 1) + " in a year.." )
