user_input = input('Please enter any string:  ')
user_tuple = tuple(user_input)
print(user_tuple)

for i in user_tuple:
    print(i)

print(type(user_tuple))
