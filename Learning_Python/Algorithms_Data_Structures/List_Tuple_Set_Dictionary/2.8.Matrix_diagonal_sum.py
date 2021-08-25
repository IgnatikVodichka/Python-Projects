import random


# matrix dioganal sum
size = 3

matrix = [[random.randint(0, 100) for _ in range(size)] for i in range(size)]

print(matrix)


for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

sumd1 = 0
sumd2 = 0
for i in range(size):
    sumd1 += matrix[i][i]
    sumd2 += matrix[i][size - i - 1]

print(sumd1, sumd2)
