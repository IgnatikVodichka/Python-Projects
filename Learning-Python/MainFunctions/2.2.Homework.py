user_string = input('Please enter any string: ')

for i in range(len(user_string)):
    print(ord(user_string[i]))
    i += 1

user_num = input('Please enter a few numbers: ')

if user_num.isdigit():
    print('Thank You!')
elif user_num.isdigit() == False:
    print('Wrong entry')
