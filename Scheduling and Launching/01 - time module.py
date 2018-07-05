# The time module

import time

# Seconds that have passed since the Unix Epoch
# Jan 1 1970 at 12 AM
print(time.time())


# Using time to keep track of how long functions took #

# Using the Collatz sequence as an example
def funkyFunction(num):
    if num % 2 == 0:
        print(str(num //  2))
        return num // 2
    else:
        print(str(3 * num + 1))
        return 3 * num + 1

def someStupidFunction(num):
    progress = 0
    while progress == 0:
        input = num
        progress = 1

    check = funkyFunction(input)
    iteration = 2
    while check != 1:
        print('Iteration: ' + str(iteration))
        check = funkyFunction(check)
        iteration += 1


# creating some crazy big number

sNum = 3826 * 9999 * 5734 * 3287
sNum = sNum * sNum * sNum
sNum = sNum * sNum * sNum * sNum
sNum = sNum * sNum * sNum * sNum
sNum = sNum * sNum * sNum * sNum

start = time.time()
someStupidFunction(sNum)
end = time.time()

# Detracting the start time from the end time to determine how many seconds it took.
print("This function took %s seconds to complete" % (end - start)) # it took my pc 27.479 seconds..


# The sleep function #

print("Wait a second...")
time.sleep(1)
print("Thanks, now wait three seconds")
time.sleep(3)
print("KTHXBAI")


# Round numbers #

manydecimals = 253.32873205970935270932570973520
# Parameters: the number you want to round and how many decimals you want to round on
fewDecimals = round(manydecimals, 2)
print(fewDecimals)

