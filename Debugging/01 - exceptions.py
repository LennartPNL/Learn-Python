# Throwing custom exceptions

#raise Exception('Now you really broke the program!')

'''
This results in the following Traceback:
Exception: Now you really broke the program!
'''

# Inside a function

def brokenCalculator(num1, operator, num2):
    if len(operator) != 1:
        raise Exception('Invalid operator')
    if not num1.isdecimal():
        raise Exception('Invalid first number')
    if not num2.isdecimal():
        raise Exception('Invalid second number')
    print(num1, operator, num2)




for n1, op, n2 in ((10, 'ok', 12), ('four', 'x', 'ten'), (1.002, 'x', '12'), ('13', 'x', 'a'), ('12', '*', '2')):
    try:
        brokenCalculator(n1, op, n2)
    except Exception as e:
        print('Whoops: ' + str(e)) # Prints the exception for every input given in the for loop










