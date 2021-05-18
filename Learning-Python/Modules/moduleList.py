print('Hello! Welcome to our module!')

user_list = [32, 44, 5, 6, 7, 8, 89, 23]

print(user_list)


def maxnum():
    max = user_list[0]
    for i in user_list:
        if i > max:
            max = i
    return max


print(f'Maximum number in list will be {maxnum()}')


def minnum():
    min = user_list[0]
    for i in range(len(user_list)):
        if user_list[i] < min:
            min = user_list[i]
    return min


print(f'Minimum number in list will be {minnum()}')


def sumnum():
    i = 0
    s = 0
    while i < len(user_list):
        s += user_list[i]
        i += 1
    return s


print(f'Summ of all numbers in list will be {sumnum()}')
