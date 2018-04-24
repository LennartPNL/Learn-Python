# List Fortune Teller

import random

fortune = ['Well, yes' , 'I think not' , 'Hell yeah brudda!' , 'Absolutely not!' , 'You should' , 'Do not even think about it!' , 'Do it twice!' , 'At the sacrifice of your yougest child.']

print()
print('     #####Fortune teller 2000#####     ')
print()
print('I am not responsible for any harm done')
print()
print('type exit to stop')
print()
print()

while True:
    print('Ask your question: ')
    inp = input()
    if inp == 'exit':
        break
    else:
        answer = str(fortune[random.randint(0, len(fortune) -1)])
        print(answer)
