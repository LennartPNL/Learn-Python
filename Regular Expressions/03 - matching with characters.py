# Matching with characters

import re

# Matching with |

peopleRegex = re.compile(r'Jandino|Rob|John') # | means OR
email = 'I was on a holiday with Rob and it sucked balls' # Rob is found
foundPers = peopleRegex.search(email) 
print(foundPers.group())
print()

sweaRegEx = re.compile(r'Dick(face|head|wad|man)')
cursing = 'You damn Dickman! Shut up'
foundSwear = sweaRegEx.search(cursing)
print(foundSwear.group()) # Dickman
print(foundSwear.group(1))  # man
print()

# matching with ?

coRegEx = re.compile(r'co(ca co)?la') # ? is for optional matching

drink = 'coca cola'
drink2 = 'cola'

foundDrink = coRegEx.search(drink)
foundDrink2 = coRegEx.search(drink2)

print(foundDrink.group()) # coca cola
print(foundDrink2.group()) # cola
print()

# Matching with *

genRegex = re.compile(r'spider(wo)*man') # Finds zero or more instances of wo

spider1 = 'A ain\'t afraid of no spiderman!'
spider2 = 'There seems to be a spiderwoman situation over here'
spider3 = 'Sing along: spiderwowowowowowoman!'

foundSpider1 = genRegex.search(spider1)
foundSpider2 = genRegex.search(spider2)
foundSpider3 = genRegex.search(spider3)

print(foundSpider1.group())
print(foundSpider2.group())
print(foundSpider3.group())
print()

# Matching with +

genRegexPlus = re.compile(r'spider(wo)+man') # Finds one or more matches

foundSpiderPlus1 = genRegexPlus.search(spider1)
foundSpiderPlus2 = genRegexPlus.search(spider2)
foundSpiderPlus3 = genRegexPlus.search(spider3)

print(foundSpiderPlus1) # None, so grouping is impossible
print(foundSpiderPlus2.group())
print(foundSpiderPlus3.group())
print()

# Matching with {}

santaRegex = re.compile(r'(ho){3}') # this is the same as (ho)(ho)(ho)

print(santaRegex.search('Well, hohohohohoho').group()) # Returns hohoho
# This works only whe the amout of ho's are the same as in the {}
print()

manyHoes = 'hohohohohohoho errrr'
mostSantaRegex = re.compile(r'(ho){1,4}') # search for 1 till 4 ho'
leastSantaRegex = re.compile(r'(ho){1,4}?')

print(mostSantaRegex.search(manyHoes).group()) # returns four ho's, this one is greedy
print(leastSantaRegex.search(manyHoes).group()) # this returns one ho, it is a nongreedy expression


