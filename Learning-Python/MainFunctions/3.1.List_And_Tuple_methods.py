user_list = [1, 2, 3, 4, 5]
user_list[0] = 2
print(user_list)
user_list.append(9)  # adds an element to the end of the list
print(user_list)

user_list.extend([0, 1, 34, 82])  # extends a list by some number of elements
print(user_list)

user_list.insert(0, 5)  # inserts element to list in the 0 position(index)
print(user_list)

print(user_list.index(0))  # calls for element's '0' index
print(user_list.count(0))  # counts how many time element '0' is in the list

user_list.reverse()
print(user_list)  # makes list to be backwards

user_list.remove(82)  # deletes element 82 from the list
print(user_list)

# deletes element by it's index i.e '3', so element '9' will be deleted
user_list.pop(3)
print(user_list)
user_list.clear()  # completeley erases the list to make it empty
print(user_list)

user_list = [0, 4, 8, 2, 1, 3, 10, 5]
print(user_list)

user_list.sort()  # sorts the list from smallest number to greatest
print(user_list)

# sorts the list from greatest to smallest numbers
user_list.sort(reverse=True)
print(user_list)

# with tuple you can do same operations except the ones that change tuple, because tuples can't be changed.
