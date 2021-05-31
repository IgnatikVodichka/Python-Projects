# 1.Deleting element from the list durin iteration of this list:

list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5]
list_3 = [1, 2, 3, 4, 5]
list_4 = [1, 2, 3, 4, 5]

# The del statement works by unbinding the name, removing it from the set of names known to the Python interpreter.
# If this variable was the last remaining reference to an object, the object will be removed from memory.
# If, on the other hand, other variables still refer to this object, the object won't be deleted.
# 'del' command works with specific index. And doesn't return anything.
for i, item in enumerate(list_1):
    del item
print(list_1)


# In this example we actually deleted only 2 itmes from the list.Loop worked, but when it started to iterate the list
# from the first element '1',  index and elements moved so the next element it saw was not '2' but '3' and after that
# due to the same reason the loop finished it's work.
# .remove deals with elemetns not indexes.
for i, item in enumerate(list_2):
    list_2.remove(item)
print(list_2)

# same situation as with remove.
# pop() works with index.Returns the velue that it removed.
for i, item in enumerate(list_3):
    list_3.pop(i)
print(list_3)


# Here deleting(removing) procees was carried out from the list, while loop moved through it's slice(virtual copy of the list)
for i, item in enumerate(list_4[:]):
    list_4.remove(item)
print(list_4)
