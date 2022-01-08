

# save only unique values:

lst = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7,
       8, 64, 22, 3, 45, 6567, 32, 1, 2, 3, 4, 5]
lst = list(set(lst))  # pushing from list to set and back to list again.
print(lst)
