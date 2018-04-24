# The List Data Type


# Adding items to my list
somelist = ['fish', 'frog', 'funky jesus']

# Printing items form a list -> They start at 0
print(somelist[0])
print(somelist[1])
print(somelist[2])

# A list can also contain a list

trickyList = [['apple', 'oragnge' , 'melon', 'mango'] , ['cat' , 'dog' , 'cow']]

print(trickyList[0][2]) # Prints melon
print(trickyList[1][1]) # Prints dog

# You can use negative index numbers

print(trickyList[-1][-1]) # This points to the last list and it's last item
print(trickyList[0][-1]) # This one points to the first list's last item

# Getting Slices from a sublist

print(trickyList[0][2:4]) # Prints item 2 to 4 (2 and 3) of the first list

print(trickyList[1][2:]) # Prints FROM 2 to everything afterwards

print(trickyList[0][:2]) # Prints UNTIL 2 and everything before

# List Length

print(len(somelist))

# Concatinate Lists

fancyList = [somelist] + trickyList

print(fancyList)

# Remove values from a list

del fancyList[0][1] # Delete frog

print(fancyList)

# Lists as replacements of a shitload of variables

print()
print('#####Time for Hobbies#####')
print()

hobbies = []

while True:
    print('Enter hobby no. ' + str(len(hobbies) + 1) + ' or type exit to stop.')
    hobby = input()
    if hobby == 'exit':
        break
    hobbies = hobbies + [hobby]
print('Your ' + str(len(hobbies)) + ' hobbies are: ')
for hobby in hobbies:
    print(' - ' + hobby)

