# The Dictionary 

sandwich = {'size:': 'small', 'smell': 'dank', 'price': 'cheap'} # Create dictionary

print(sandwich['smell']) # Prints dank

print('My sandwich is very ' + sandwich['price'] + '.')

# In essence, a dictionary is an unordered list

list1 = ['ed' , 'edd' , 'eddy']

list2 = ['fred' , 'fredd' , 'freddy']

print(str(list1 == list2)) # Evaluates to False

dict1 = {'size:': 'small', 'smell': 'dank', 'price': 'cheap'}

dict2 = {'smell': 'dank', 'price': 'cheap', 'size:': 'small'}

print(str(dict1 == dict2)) # Evaluates to True, it holds the same information in a different order 

# Example of dictionary

weightClass = {'John': 'Fat', 'Ron': 'Heavy bones', 'Nena': 'Luftballon'}


while True:
    print('Whose weight class would you like to know? (type exit to exit)')
    person = input()
    if person == 'exit':
        break

    if person in weightClass:
        print('Well, ' + person + ' is in weight class: ' + weightClass[person])
    else:
        print('Who is ' + person + '?')
        print('What weight class is ' + person + ' in?')
        newPersonWeightClass = input()
        weightClass[person] = newPersonWeightClass # Adding the person with his/her weight class to the dictionary
        print('We added ' + newPersonWeightClass + ' for ' + person + '.')


