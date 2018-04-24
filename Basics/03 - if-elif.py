# if/elif example


print('enter name: ')
name = input() # input() waits for user input on the keyboard
print('enter age: ')
age = input()
age = int(age)

if name == 'john':
    print('Ola, Johnson')
elif age < 12:
    print('You are not John, stupid!')
elif age > 2000:
    print('I do not think you are this old')
elif age > 100:
    print('U old fool')




