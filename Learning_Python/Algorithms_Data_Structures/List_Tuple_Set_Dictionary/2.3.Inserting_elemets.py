# import random

# gen_lst = [random.randint(-100, 100) for _ in range(50)]
# print(f'{gen_lst}')

gen_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(gen_lst)

num = int(input('What number would you like to insert in the list: '))
idx = int(input('Where(which index) would you like to insert this number in list: '))

gen_lst.append(None)  # adding empty element to the list

i = len(gen_lst) - 1

while i > idx:
    gen_lst[i], gen_lst[i-1] = gen_lst[i - 1], gen_lst[i]
    i -= 1

# gen_lst.insert(idx,num) #that is the one line command to do the same.Basicly solution above is under the Python's 'hood' of command .insert
# gen_lst_new = gen_lst[:idx] +[num] gen_lst[idx:] #here we used slice in Python. This solution takes x2 times more memory due to creating a new list.

gen_lst[idx] = num
print(gen_lst)
