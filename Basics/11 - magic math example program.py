# Magic Math Example Program


def collatz(number): 
    if number % 2 == 0:
        print(str(number //  2))
        return number // 2
    else:
        print(str(3 * number + 1))
        return 3 * number + 1
 

# Ask the user for any integer input
def userInputCollatz():
    print('Enter a number: ')

    progress = 0
    while progress == 0:
        try:
            userInput = int(input())
            progress = 1
        except ValueError:
            print('That is not an integer!')
            print('Enter a number: ')
            progress = 0
        

    check = collatz(userInput)
    iteration = 2
    # The Collatz Sequence will always reach one
    while check != 1:
        print('Iteration: ' + str(iteration))
        check = collatz(check) # recursion
        iteration += 1



userInputCollatz()    
