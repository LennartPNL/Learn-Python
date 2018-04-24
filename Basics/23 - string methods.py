# String Methods

scream = 'I am not angry at all.'

# upper()

print(scream.upper()) # All caps
print()

whisper = 'WHAT?'

# lower()

print(whisper.lower()) # All lower
print()

# Example

print('Type Y for a goof')
userInput = input()
if userInput.upper() == 'Y': # Typing y will result in Y
    count = 0
    while count < 100:
        print("a goof")
        count = count + 1
else:
    print('Ok, go then.')

print()

# isupper() and islower()

upper = 'OH DAMN'
lower = 'i see'

print(upper.isupper()) # True
print(lower.islower()) # True
print(lower.isupper()) # False
print(lower.upper().isupper()) # True

print()


# isalpha(), isalnum(), isdecimal(), isspace() and istitle()

alpha = 'hey'
print(alpha.isalpha()) # True when string only contains letters and is not empty

alnum = 'h4ck3r'
print(alnum.isalnum()) # True when string only contains letters and numbers and is not empty

decimal = '9876'
print(decimal.isdecimal()) # True when string only contains numeric characters and is not empty

space = '    \t\n'
print(space.isspace()) # True when string only contains a space, \n or \t and is not empty

title = 'This Is My Title'
# True when string only contains words starting with a capital letter and is followed by lower case letters
print(title.istitle())

print()

# Example

while True:
    print('enter your IQ to win a meet and greet with baby Jesus')
    iq = input()
    if iq.isdecimal():
        print('God is dead, abandon all hope')
        break
    print('IQ is a number... You ain\'t gonna see lil\' Jesus!')

# startswith() and endswith()

print()

startswith = 'Starting with'
print(startswith.startswith('Starting')) # True

endswith = 'Starting with the end'
print(endswith.endswith('end')) # True

# Splitting and Joining

apes = ['Bokito' , 'Harambe', 'Trump']
joinWith = ' and '
joined = joinWith.join(apes)
print('My favourite apes are ' + joined) # Joins the apes list into one string

print()

splitted = joined.split()

print(splitted) # Prints a list of words, by default splitted by a space

print()

unreadable = 'If$You$Would$Like$To$Read$This,$You$Should$Split'
readable  = unreadable.split('$')
print(readable)











