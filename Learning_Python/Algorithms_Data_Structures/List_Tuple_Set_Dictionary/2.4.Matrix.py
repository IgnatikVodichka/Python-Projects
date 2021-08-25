import random


size = 5  # this will be the size of matrix

matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
print(matrix)
print('*'*30)
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
