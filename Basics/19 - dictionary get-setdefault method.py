# Get and Setdefault Method in Dictionaries

inMyFridge = {'ketchup': 1, 'beer': 18, 'brocolli': 1}

# It's ketchup, 0 so  the default returned value is 0

print('I have ' + str(inMyFridge.get('ketchup' , 0)) + ' bottle of ketchup in my fridge')

print('I have ' + str(inMyFridge.get('harry' , 0)) + ' harries in my fridge')

# Set default

inMyFridge.setdefault('gypsy tears', 5)

print(inMyFridge)


