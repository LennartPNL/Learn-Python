# Pattern Matching Without Regualr Expressions

def isPhoneNo(userInput): # For American Phone Numbers (i.e 125-555-8768)
    if len(userInput) != 12: # 12 characters long
        return False

    for i in range(0,3): # check if first 3 chars are numbers
        if not userInput[i].isdecimal():
            return False

    if userInput[3] != '-': # Check if fourth char is a -
        return False

    for i in range(4, 7): #Check if fifth to eigth chars are numbers
        if not userInput[i].isdecimal():
            return False

    if userInput[7] != '-': # Check if eigth char is a -
        return False

    for i in range(8, 12): # Check if ninth to twelfth chars are numbers
        if not userInput[i].isdecimal():
            return False

    return True # Got through all checks, so it is a phone number 

print(isPhoneNo('This is not a phone number')) # False
    
print(isPhoneNo('222-888-7253'))    # True        
    
print()


email = 'Heyy, wanna check my skittles tomorrow? call me: 232-767-2736 ok?'

for i in range(len(email)): # Range is the length of the massage
    part = email[i:i+12] # Index ranges between i and 12 (length of phone number)
    if isPhoneNo(part): 
        print('Message contains phonenumber: ' + part)
print('Bye!')
