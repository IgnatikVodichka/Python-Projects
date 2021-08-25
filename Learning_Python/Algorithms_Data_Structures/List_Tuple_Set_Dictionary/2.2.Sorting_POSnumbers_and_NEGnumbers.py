import random


gen_lst = [random.randint(-100, 100) for _ in range(50)]
print(f'Unsorted: {gen_lst}')
neg_lst = []
pos_lst = []

for item in gen_lst:

    if item < 0:
        neg_lst.append(item)

    elif item > 0:
        pos_lst.append(item)

print(f'Negative: {neg_lst}')
print(f'Positive: {pos_lst}')


# second option which is not so good because here we are going through list twice. One time to take out all negative numbers and second time to take out all positive numbers.
neg_lst1 = [item for item in gen_lst if item < 0]
pos_lst1 = [item for item in gen_lst if item > 0]
