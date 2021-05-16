user_dict = {'Name': 'No Name', 'Age': '-1'}
user_name = input('Please enter your name: ')
user_age = input('Please enter your age: ')

user_dict = {'Name': user_name, 'Age': user_age}

for key in user_dict:
    print(f'{key} = {user_dict[key]}')
