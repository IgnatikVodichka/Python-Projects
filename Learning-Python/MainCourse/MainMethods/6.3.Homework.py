import shutil
print('Please enter 1 - to read file ; 2 - to write to file ; 3 - to copy file')
user_command = input()

if user_command == '1':
    user_input = str(input('Please enter a file path: '))
    user_file = open(user_input, 'r')
    print(user_file.read())
    user_file.close()

if user_command == '2':
    user_input = str(input('Please enter a file path: '))
    user_file = open(user_input, 'a')
    user_text = str(input('Please enter what you want to write to file: '))
    user_file.write(user_text)
    user_file = open(user_input, 'r')
    print(user_file.read())
    user_file.close()

if user_command == '3':
    user_input = str(input('Please enter a file path: '))
    user_path = str(
        input('Please enter the path where you want to copy file: '))
    shutil.copy2(user_input, user_path)
