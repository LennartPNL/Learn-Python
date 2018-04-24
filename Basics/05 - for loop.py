# The for loop and range() funtion

for i in range(5): # This loops intil it has reached it's range of 5
    print('I printed ' + str(int(i + 1)) + ' time/times.')


# Adding up the sum of the numbers 0 to 100

total = 0
for number in range(101):
    total = total + number
print(total) # Which adds up to 5050

# Passing parameters to the range() function

for i in range(100, 110):
    print(i) # This will print 100 / 109 -> all numbers between 100 and 110

# One more parameter

for i in range(10, 21, 5):
    print(i) # Prints all numbers between 10 and 21, with an interval of 5

# This also works for a countdown

for i in range(10, -1, -1):
    print(i)

