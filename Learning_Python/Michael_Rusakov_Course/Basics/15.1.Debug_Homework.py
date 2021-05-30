user_list = []

while len(user_list) != 10:
    user_input = (int(input('Please enter numbers including negative: ')))
    user_list.append(user_input)

print(user_list)


def negative_number(user_list):
    i = 0
    n = 0
    while n <= len(user_list):
        for i in (user_list):
            if i < 0:
                print(i)
                i += 1
        break


negative_number(user_list)
