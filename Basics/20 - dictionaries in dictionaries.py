# Dictionaries in Dictionaries

peoplesFridgeContents = {'rob': {'mothermilk': 6, 'beer': 0, 'lego': 1},
                         'alice': {'cheese': 2, 'beer': 4, 'cucumber': 2},
                         'sid': {'cheese': 1, 'beer': 12, 'sprite': 1} 
                         }

def countItems(person, item):
    total = 0
    for key, value in peoplesFridgeContents.items():
        total = total + value.get(item, 0)
    return total

print('If we were to host a fridge party, we would have: ')
print(str(countItems(peoplesFridgeContents, 'mothermilk')) + ' Mothermilk')
print(str(countItems(peoplesFridgeContents, 'beer')) + ' Beer')
print(str(countItems(peoplesFridgeContents, 'lego')) + ' lego')
print(str(countItems(peoplesFridgeContents, 'cheese')) + ' Cheese')
print(str(countItems(peoplesFridgeContents, 'cucumber')) + ' Cucumber')
print(str(countItems(peoplesFridgeContents, 'sprite')) + ' sprite')
