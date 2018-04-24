# Exception handling

def devider(toDevide, devideBy):
    return toDevide / devideBy

print(devider(10, 2))
print(devider(12, 4))
# print(devider(7, 0)) -> This will cause an error

# To prevent this error:

def deviderBetter(toDevide, devideBy):
    try:
        return toDevide / devideBy
    except ZeroDivisionError:
        print('Error: you cannot devide by 0...')

print(deviderBetter(80, 2))
print(deviderBetter(17, 4))
print(deviderBetter(10, 0)) # This prints out the error message

