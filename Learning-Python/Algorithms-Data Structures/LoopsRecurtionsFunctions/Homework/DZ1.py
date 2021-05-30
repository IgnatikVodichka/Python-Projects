

while True:
    print('Please enter action to be performed with numbers: ')
    print('"0"-Exit ; "+" addition ; "-" subtraction ; "/" division ; "*" multiplication')
    a = input('Action: ')
    if a == '0':
        break
    if a in {'+', '-', '/', '*'}:
        x = float(input('Please enter first number: '))
        y = float(input('Please enter second number: '))
        if a == '+':
            print(f'The result is {x + y}')
        elif a == '-':
            print(f'The result is {x - y}')
        elif a == '*':
            print(f'The result is {x * y}')
        elif a == '/':
            if y != 0:
                print(f'The result is {x / y}')
            else:
                print()
                print("Cant' devide by zero")
                print()
                continue
    else:
        print()
        print('Wrong action')
        print()
