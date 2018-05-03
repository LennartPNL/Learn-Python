# Regex methods and classes

import re

# findall() method

phoneReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

nums = 'phones! 262-328-8839 206-697-7244 540-615-6462 yes!'

print(phoneReg.findall(nums)) # returns a list of strings, the .group() returns a Match object
print()

# Character classes

specRegex = re.compile(r'[!@#$%^&]') # Custom character class

swear = 'For F#@$k\'s sake Hagrid! I\'m not a F&^king wizard!'

print(specRegex.findall(swear)) # returns ['#', '@', '$', '!', '&', '^', '!']

# using ^ and $

startRegex = re.compile(r'^harry') # ^ means a string should start with whathever you put after the ^
print(startRegex.findall('harry, you are a c*&t')) # harry
print(startRegex.findall('c*&t, you are a harry')) # empty
print()

endRegex = re.compile(r'harry$')
print(endRegex.findall('harry, you are a c*&t')) # empty
print(endRegex.findall('c*&t, you are a harry')) # harry
print()

# The wildcard

wildRegex = re.compile(r'.opper') # finds opper and any character before that (no white spaces)
words = 'slopper flopper and a whopper'
print(wildRegex.findall(words))
print()

# Match everything .*

tagRegex = re.compile(r'<.*?>')
# without the ?, this expression is greedy, which means it finds everything between <>
# so the whole string..

html = '<p>i forgot how to html<p><br/><br/><a href="goggle.coome">do not click<a>'

print(tagRegex.findall(html)) # gets all tags
print()

# Case sensitivity

skitRegex = re.compile(r'skittle', re.I) # re.I makes it case insensitive

print(str(skitRegex.findall('i love SkIttLes')).lower()) # returns a small skittle

# Substitute strings

safeRegex = re.compile(r'is \w+', re.I)

myPass = 'Hey Johnny, my Password Is skittle12345'

print(safeRegex.sub('*****', myPass)) # substitutes the found myPass with *****








