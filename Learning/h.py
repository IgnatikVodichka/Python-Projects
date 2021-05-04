list = ['h', 'e', 'l', 'l', 'o']  # creates an array with elements inside
print(list[0])  # indexing starts from 0,1,2,3,4...100 and so on.

# -1, -2, -3... and so on means you are asking for element from the end. First element from the end and so on.
print(list[-1])

name = 'Ignat'
# function 'len' returnes the length of string or list.
print(f'Length of the list is {len(list)}')
print(f'Length of the name {len(name)}')
print(f'Last element is {list[len(list) - 1]}')  # same as (list[-1])

print('-------------')

i = 0
# this cycle will give us all the element untill it reaches the end of the list.
while i < len(list):
    print(list[i])
    i += 1

# with the list[3] = a you can change value of third element in the array
# velues in the list can be of any type

print('-------------')

# inside one list you can include as many other lists as you like
list2 = [[1, 2], 3, '4', 5.7, 'a', [True, False]]
# e.g. [1,2] index will be 0
print(list2[0])
print(list2[-1])

print('-------------')

list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # how to iterate 2+dimensional list
i = 0
while i < len(list3):
    j = 0
    while j < len(list3[i]):
        print(list3[i][j])
        j += 1
    i += 1

print('-------------')

# how to find smallest and greates value from the list
prices = [20, 40, 50, 15, 32, 80]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1

print(f'Min value from the list {min}')
print(f'Max value from the list {max}')
