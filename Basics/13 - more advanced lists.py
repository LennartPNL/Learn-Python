# Lists More Advanced

# Loops and lists

inMyBag = ['pen' , 'book' , 'sandwich' , 'rope']

for i in range(len(inMyBag)):
    print('Index no. ' + str(i) + ' holds a ' + inMyBag[i]) # Everything in my bag

# The in/not in operators

print('There is a pen in my bag: ' + str('pen' in inMyBag)) # True
print('There is a cat in my bag: ' + str('cat' in inMyBag)) # False

print()
print('#####Check Yo Bag!#####')
print()
print('Enter an item or type stop to stop ')

while True:
    check = input()
    if check == 'stop':
        break
    elif check not in inMyBag:
        print(check + ', that is not in my bag!')
    else:
        print(check + ', that is in my bag!')


# Augmented Assignment of lists

dupesInMyBag = inMyBag * 3

print(dupesInMyBag) # Three times the stuff in my bag!

# Finding values in a list

print(dupesInMyBag.index('pen')) # Shows first occurence of pen in the list (0)

# Adding values to your list

inMyBag.append('tortelini') # Adds tortelini to the end of the list
print(inMyBag)

inMyBag.insert(2, 'coffee') # Adds coffee to index number 2
print(inMyBag)

# Removing values from the list

inMyBag.remove('pen') # Remove the pen value from the list
print(inMyBag)

# Sorting values in a list

myGrades = [8, 2, 4, 6]
myGrades.sort()
print(myGrades) # Sorted numbers ascending
inMyBag.sort()
print(inMyBag)  # Sorted strings alphabetically ascending
inMyBag.sort(reverse=True)
print(inMyBag)  # Sorted strings alphabetically descending





