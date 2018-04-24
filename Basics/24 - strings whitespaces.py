# Whitespaces in strings

left = 'Whaddup?'
print(left.ljust(10) + '.') # Adds ten white spaces after Whaddup?
right = 'Awesome'
print('.' + right.rjust(10)) # Adds ten white spaces before Awesome
center = 'Bye'
print('.' + center.center(10) + '.') # Adds ten white spaces before and after Bye
between = 'WOWZERZ'
print('.' + between.center(25, '#') + '.') # Makes the string 25 characters wide, filled up with '#'

print()

# Example

inMySack = {'Pen': 2, 'Book': 0, 'Charger': 3, 'Sock': 5}

def printSack(dictionary, left, right):
    print(' In your Sack '.center(left + right, '#'))
    for key, value in dictionary.items():
        print(key.ljust(left, '_') + str(value).rjust(right))

printSack(inMySack, 25, 1)
print()
printSack(inMySack, 50, 12)

print()

# Removing whitespaces

leftStrip = '     Hey.'
print(leftStrip.lstrip()) # Removes whitespaces on the left
rightStrip = 'Hay.     '
print(rightStrip.rstrip()) # Removes whitespaces on the right
bothStrip = '     Hello     '
print(bothStrip.strip()) # Removes whitespaces on both sides
stripStuff = 'Password'
print(stripStuff.strip('ord')) # Removes ord on the end of the string

print()


