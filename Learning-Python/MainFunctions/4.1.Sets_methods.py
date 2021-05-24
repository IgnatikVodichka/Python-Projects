set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8, 9, 0, 10}
print(type(set1))
print(set1)
print(set2)

set1.add(10)  # adds the element to the set.
print(set1)

# removes the element from the set. But if there is no such element in the set it will return error.
set1.remove(10)
print(set1)
# .discard method works same as .remove but if there is no such element it will not return error.
set1.discard(0)

# easy way to check if all the elements are the same in both sets.
print(set1 == set2)
print(set1 <= set2)  # checking if all elements of set1 are incleded in set2.
print(set1 >= set2)  # checking if all elements of set2 are incleded in set1.

# checking if all elements of set1 are incleded in set2.
print(set1.issubset(set2))
# checking if all elements of set2 are incleded in set1.
print(set1.issuperset(set2))

set3 = set1.union(set2)  # unites two sets in one set
print(set3)
print(type(set3))
set4 = set1.intersection(set2)  # only unites same elemetns from both sets.
print(set4)
# .difference method returns SET1 - SET2, so SET5 contains elements from SET1 but not in SET2
set5 = set1.difference(set2)
print(set5)
set6 = {1, 3, 6, 8, 0}
set6.clear()  # erases all elements in the set
print(set6)
set5.pop()
print(set5)  # deletes one element from set
