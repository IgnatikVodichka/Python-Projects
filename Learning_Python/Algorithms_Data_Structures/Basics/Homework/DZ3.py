import random
from random import randint
from random import randrange

a = (input('Please enter start: '))
b = (input('Please enter end: '))
choice = input(
    'Please pick one option to create: \n To create one random integer enter 1; \n To create one random real number enter 2; \n To create one random symbol letter enter 3; \n What is your choice:   ')

if choice == '1':
    a = int(a)
    b = int(b)
    result = random.randint(a, b)

elif choice == '2':
    a = float(a)
    b = float(b)
    # .uniform returns a random floating number between the two specified numbers (both included).
    result = random.uniform(a, b)
    print(f'{result:.3f}')

elif choice == '3':
    a = ord(a)
    b = ord(b)
    result = chr(random.randint(a, b))

else:
    print('Undefiened')

print(result)
