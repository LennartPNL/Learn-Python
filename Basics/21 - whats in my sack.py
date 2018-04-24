# What's in my sack

mySack = {} # Initiate your sack

# Show what is in your sack

def showSack(dictionary):
    print('This is in your sack:')
   
    for x in dictionary.keys():
        print(str(dictionary[x] + ' ' + x))
    
        
        
# Add stuff to you sack    

def addToSack(dictionary):
    print('type exit to exit or show to show what is in your sack')
    while True:
        
        print()
        print('Item to add: ')
        item = input()

        if item == 'exit':
            showSack(dictionary)
            break
        
    
                
        print('How many items of ' + item + ' do you have?' )
        amount = input()
        dictionary[item] = amount
        print(str(amount) + ' of ' + item + ' added to your sack!')
        
    
addToSack(mySack)

