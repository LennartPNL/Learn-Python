# String Manipulation - The Basics

quoteString = "My dog's nose is always wet" # Using double quotes allows you to type dog's

anotherQuoteString = 'My dog\'s pants are small' # Here \ is used as an escape character

escapeChars = ' Hoa \n Lee \n Sheet\n That \t Is \t Sweet' # \n is a line break, \t is a tab

print(escapeChars)

# Keeping the escape characters in your string

print(r'King \n Kong\'s \t Bong') # r makes the string raw, keeping everything inside intact

# Multiple line string

print()

multi = ''' Wow,
This is an amazing multiline string.
I am shocked.
Please end my suffering''' # Triple quotes

print(multi)

# Multiline comments

"""
Actually, this is not really a comment if you ask me.
But it can be used as one.
So why ask questions?
"""

# Strings can be indexed

indexedString = 'Now, that\'s what i call a hippo!'

print()

print(indexedString[17]) # i is the 17th index of that sentence

print()

print(indexedString[-6:-]) # hippo is the word in the -6:-1 range






