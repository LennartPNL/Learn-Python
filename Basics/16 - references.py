# References

def ref(param):
    param.append('cool') # Param refers to the same list as lilList

lilList = ['that' , 'is' , 'kinda']

ref(lilList)

print(lilList)

# Copy function

import copy

oneList = ['C' , 'D' , 'E']
twoList = copy.copy(oneList) # Duplicate copy, stored in different reference
twoList[0] = 'See'

print(oneList)
print(twoList)


