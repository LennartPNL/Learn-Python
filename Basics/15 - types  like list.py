# Types like a list

sentence = 'Lalalala La Bamba!'

# Strings can be manipulated like lists
print(sentence[12]) # Prints B, spaces are not counted

print('This sentence contains la: ' + str('la' in sentence)) # True
print('This sentence contains beer: ' + str('beer' in sentence)) # False
print('This sentence does not contain lo: ' + str('lo' not in sentence)) # True

# Loop over a string

for i in sentence:
    print('##### ' + i + ' #####')

# Tuple data type

tupleExample = ('cat' , 'goat' , 29 , 'spaghetti')
# Tuples are immutable, you cannot modify, remove or append values
# tupleExample[1] = 'chicken' will not work!
print(tupleExample[1])

# Converting to lists and tuples

# From list to tuple:

print(tuple(['fish' , 'fred' , 'Fries']))

# From tuple to list:

print(list(('soup' , 'bread' , 'pepper')))

# From string to list:

print(list('Whaddup?'))

