array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)

# print(sum(array))
#print(sum(array) / 5)

total = 0
for ele in range(len(array)):
    total = total + array[ele]
div = total / array[-1]
print(f'Total sum of elements: {total} ')
print(f'Total sum of elements: {div} ')

x = 0
s = 0
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while x < len(array1):
    s = s + array[x]
    x += 1
c = s / array[-1]
print(f'Total sum of elements: {total} ')
print(f'Total sum of elements: {c} ')
