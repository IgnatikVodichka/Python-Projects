import random


def bin_search(array, value):
    left = 0
    right = len(array)-1
    pos = len(array) // 2

    while array[pos] != value and left <= right:

        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1
        pos = (left+right) // 2

    return -1 if left > right else pos


a = [random.randint(0, 1000) for _ in range(0, 100)]
print(a)
b = []

# sorting the list
# i indicates how many time we sorted
for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        if a[min_index] > a[j]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]
b = a
print(b)


n = int(input('Which elemet would you like to find: '))
print(bin_search(b, n))
