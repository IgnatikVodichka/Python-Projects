
while True:
    print('1 - Write to file ; 2 - Read file ; 0 - Exit')
    user_input = input('Enter command: ')
    if user_input == '0':
        exit(0)

    elif user_input == '1':
        text_input = input('Enter what you want to write in file: ')
        user_file = open('user_file.txt', 'w')
        user_file.write(text_input)
        user_file.close()

    elif user_input == '2':
        user_file = open('user_file.txt', 'rt')
        print(f'{user_file.read()}')
        user_file.close()

    else:
        print('Wrong command!')
