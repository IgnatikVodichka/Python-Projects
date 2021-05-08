import random
from random import randint
from random import randrange


from random import randint
from random import randrange

a = int(input('Please enter start: '))
b = int(input('Please enter end: '))
number = int(random.randrange(a, b))
print(number)

a = float(input('Please enter start: '))
b = float(input('Please enter end: '))
number = float(random.randrange(a, b))
print(number)

a = ord(input('Please enter start: '))
b = ord(input('Please enter end: '))
number = (random.randrange(a, b))
print(chr(number))
