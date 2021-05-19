import random
from random import randrange

user_list = [int(random.randint(0, 100)) for i in range(
    0, int(input('Please input number of elements to be on the list:  ')))]
print(user_list)
print(len(user_list))
i = 0
while i < len(user_list):
    print(user_list[i])
    i += 1

user_set = set(user_list)
print(user_set)
print(len(user_set))

print()

for i in user_set:
    print(i)
