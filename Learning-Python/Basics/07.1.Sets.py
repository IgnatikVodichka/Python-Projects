# we have created a variable in which 'set' function created a set which is unordered and unindexed
# set but here ',' sign is not allowed to be placed between the values. Set will be displayed letter by letter but not with duplicates.
myset_1 = set('PythonN''apple')

# also set but displayed differently from the first one. Here ',' is optional. Depending on using it displayed values will be showed differently.
# values here will be treated as separate words
myset_2 = {"PythoNnN", "apple"}

# values here will be connected together as one string
myset_3 = {"PythoNnN" "apple"}

print(myset_1)
print(myset_2)
print(myset_3)
print(type(myset_1))
print(type(myset_2))
print(type(myset_3))

print()

# creating a list in range from 0 to 9 (10 is not included)
list = [i for i in range(0, 10)]
print(list)

myset_4 = set(list)  # passing a 'list' to the 'set'
print(myset_4)

print()

# also you can pass 'list' to 'set' directly
myset_5 = set([1, 2, 3, 22, 2, 4, 5, 6, 7, 7, 8, 9, ])
print(myset_5)

print()

name = 'ignat'
print(name)
myset_6 = set(name)
print(myset_6)
