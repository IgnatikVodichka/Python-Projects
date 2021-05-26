import random

# creates random number from 0 to 1, but 0 is included in that and 1 is not.
arr = (random.random())
print(arr)

array = int(random.random() * 10)  # making random number an integer
print(array)

# creating random list with integers inside
array1 = [int(random.random() * 10) for i in range(1, 100)]
print(array1)
# pushing 'list' directly into 'set' to exclude all the duplicates
myset = set(array1)
print(myset)
