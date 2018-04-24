# Dictionary Keys, Items and Values

mice = {'harold': 'tiny mouse', 'rose': 'nipple mouse', 'willy wonka': 'dead mouse'}

# Looping over a dictionary

for m in mice.values(): # All values of the dictionary
    print(m)

print()

for m in mice.keys(): # All keys of the dictionary
    print(m)

print()

for m in mice.items(): # All items of the dictionary
    print(m)

print()

# Or get all info from the dictionary

for key, value in mice.items():
    print(value + ' ' + key + ' represent!')

# Checkin a dictionary for a specific value

print()

print('harold' in mice.keys()) # True
print('harold' in mice.values()) # False


