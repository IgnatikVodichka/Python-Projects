name = 'Ignat'
i = 0
while i < len(name):
    print(name[i])
    i += 1

print()

# same can be done with string instead of 'while' function on top
list1 = [1, 2, 3, 4]
for n in list1:
    print(n)

print()
a = 0
for a in name:
    if a == 'a':
        break
    print(a)
else:
    print('There is no such symbol')

print()

list2 = range(1, 10)  # makes variable with range of values
for s in list2:
    print(s)

print()

array = list(range(2, 20))  # list is also a function that creates a list
print(array)

list3 = [i for i in range(1, 21)]  # one more option how to make array
print(list3)

# all range of numbers in array will be multiplied by 2.
list4 = [i * 2 for i in range(1, 21)]
print(list4)

# all range of numbers in array will be only even numbers
list5 = [i for i in range(1, 21) if i % 2 == 0]
print(list5)

print('----------')

n = 2  # one more way to display all even numbers
while n <= 100:
    n = n+2
    print(n)

print('----------')

# and one more way to display array of even numbers
array2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
n = 0
while n < 10:
    i += 2
    array2[n] = i
    n += 1
print(array2)
